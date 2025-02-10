import boto3
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

BUCKET_NAME = "seu-bucket-aqui"
MAX_WORKERS = 20
BATCH_SIZE = 1000

def delete_batch(s3, bucket, objects_batch, max_retries=5):
    delay = 1
    for attempt in range(max_retries):
        try:
            response = s3.delete_objects(Bucket=bucket, Delete={"Objects": objects_batch, "Quiet": True})
            return response
        except Exception as e:
            if attempt == max_retries - 1:
                raise e
            time.sleep(delay)
            delay *= 2

def main(bucket_name):
    s3 = boto3.client("s3")
    paginator = s3.get_paginator("list_object_versions")
    objects_to_delete = []
    futures = []
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        for page in paginator.paginate(Bucket=bucket_name):
            versions = page.get("Versions", [])
            delete_markers = page.get("DeleteMarkers", [])
            keys_with_marker = {marker["Key"] for marker in delete_markers}
            for version in versions:
                if version["Key"] in keys_with_marker:
                    objects_to_delete.append({"Key": version["Key"], "VersionId": version["VersionId"]})
            for marker in delete_markers:
                objects_to_delete.append({"Key": marker["Key"], "VersionId": marker["VersionId"]})
            while len(objects_to_delete) >= BATCH_SIZE:
                batch = objects_to_delete[:BATCH_SIZE]
                objects_to_delete = objects_to_delete[BATCH_SIZE:]
                futures.append(executor.submit(delete_batch, s3, bucket_name, batch))
        if objects_to_delete:
            futures.append(executor.submit(delete_batch, s3, bucket_name, objects_to_delete))
        for future in as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print("Erro ao deletar um lote:", e)
                return
    print("Processo de limpeza concluído.")

if __name__ == "__main__":
    main(BUCKET_NAME)

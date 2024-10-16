import logging
import azure.functions as func
def main(inputblob: func.InputStream, outputblob):
logging.info(f"Python blob trigger function processed {inputblob.name}.")
outputblob.set(inputblob)
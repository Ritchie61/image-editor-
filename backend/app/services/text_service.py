import easyocr

reader = easyocr.Reader(["en"])

async def extract_text(file):
    file_path = f"temp/{file.filename}"
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    text_data = reader.readtext(file_path, detail=0)
    return {"text": text_data}

def edit_text(data):
    return {"message": "Text edited successfully", "data": data}

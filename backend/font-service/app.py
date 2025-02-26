from fastapi import FastAPI, UploadFile, File
import fontTools.ttLib

app = FastAPI()

@app.post("/match-font")
async def match_font(file: UploadFile = File(...)):
    font = fontTools.ttLib.TTFont(io.BytesIO(await file.read()))
    return {"matched_font": font["name"].getDebugName(1)}

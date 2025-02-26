import React, { useEffect, useRef } from "react";
import { fabric } from "fabric";

const Canvas = ({ file }) => {
    const canvasRef = useRef(null);

    useEffect(() => {
        const canvas = new fabric.Canvas(canvasRef.current, {
            backgroundColor: "#f9f9f9",
        });

        if (file) {
            const reader = new FileReader();
            reader.onload = (e) => {
                fabric.Image.fromURL(e.target.result, (img) => {
                    img.scaleToWidth(500);
                    canvas.add(img);
                    canvas.renderAll();
                });
            };
            reader.readAsDataURL(file);
        }
    }, [file]);

    return <canvas ref={canvasRef} width="600" height="400"></canvas>;
};

export default Canvas;

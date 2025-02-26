import React, { useState } from "react";
import { useDropzone } from "react-dropzone";
import { uploadFile } from "../api/fileApi";

const Upload = ({ onFileUpload }) => {
    const [uploading, setUploading] = useState(false);

    const { getRootProps, getInputProps } = useDropzone({
        accept: "image/*",
        onDrop: async (acceptedFiles) => {
            setUploading(true);
            const file = acceptedFiles[0];
            try {
                const response = await uploadFile(file);
                onFileUpload(file);
            } catch (error) {
                console.error("Upload failed:", error);
            }
            setUploading(false);
        }
    });

    return (
        <div {...getRootProps()} className="upload-area">
            <input {...getInputProps()} />
            <p>Drag & drop an image, or click to select a file</p>
            {uploading && <p>Uploading...</p>}
        </div>
    );
};

export default Upload;


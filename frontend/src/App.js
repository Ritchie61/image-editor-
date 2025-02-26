import React, { useState } from "react";
import Upload from "./components/Upload";
import Canvas from "./components/Canvas";
import Toolbar from "./components/Toolbar";
import Sidebar from "./components/Sidebar";
import "./styles.css";

const App = () => {
    const [file, setFile] = useState(null);
    const [selectedItem, setSelectedItem] = useState(null);

    return (
        <div className="app-container">
            <h1>Image & Text Editor</h1>
            <Upload onFileUpload={setFile} />
            <Toolbar />
            <div className="workspace">
                <Canvas file={file} />
                <Sidebar selectedItem={selectedItem} />
            </div>
        </div>
    );
};

export default App;

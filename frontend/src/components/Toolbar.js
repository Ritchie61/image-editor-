import React from "react";

const Toolbar = ({ onAddText }) => {
    return (
        <div className="toolbar">
            <button onClick={onAddText}>Add Text</button>
        </div>
    );
};

export default Toolbar;

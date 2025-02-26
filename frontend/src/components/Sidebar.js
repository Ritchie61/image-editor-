import React from "react";

const Sidebar = ({ selectedItem }) => {
    return (
        <div className="side-panel">
            <h3>Properties</h3>
            {selectedItem ? (
                <p>Selected: {selectedItem.type}</p>
            ) : (
                <p>No selection</p>
            )}
        </div>
    );
};

export default Sidebar;

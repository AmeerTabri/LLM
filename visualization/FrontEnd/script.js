/* Global Variables */

// handle parts and node states
let currPart = 1;
let numOfParts = 1;
let openedNodesState = {};

// handle edge case alerts
let isMarkDownDroped = [];
let isDataDroped = false

// save open windows
let openedWindow = [];  

function getNodesStatus(obj) {
    let result = {}; 
 
    if (obj.children && Array.isArray(obj.children) && obj.children.length > 0) {
        // Add to result only if it has children - no need for leafs
        if (obj.hasOwnProperty('name') && obj.hasOwnProperty('isOpen')) {
            result[obj.name.split(" ")[0]] = obj.isOpen;
        }
 
        obj.children.forEach(child => {
            let childResult = getNodesStatus(child);
            result = { ...result, ...childResult };  
        });
    }

    return result;  
}

// Function to handle the drop event for Markdown files
function handleMdDrop(event) {
    event.preventDefault();
    const file = event.dataTransfer.files[0];
    const reader = new FileReader();

    reader.onload = function (e) {
        const markdownData = e.target.result;  
        console.log(markdownData); 
 
        fetch('http://127.0.0.1:5000/markdown', {
            method: 'POST',
            headers: {
                'Content-Type': 'text/plain',   
            },
            body: markdownData,   
        })
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();  
        })
        .then(jsonData => {
            console.log('Received JSON:', jsonData);   
            parseJsonData(jsonData);  

            isMarkDownDroped[currPart] = true; 
         
            d3.select("svg").remove();
         
            drawTree(jsonData);
            
            // Hide the drop area after successful upload
            const dropZone = document.getElementById('drop-zone-md');
            dropZone.style.display = 'none';  
            
            // Show the download button
            const download = document.getElementById('download-btn');
            download.style.display = 'flex'; 
        }) 
        .catch(error => {
            console.error('Error:', error);
            alert("Markdown file does not correspond with data file");
        });
    };

    reader.readAsText(file);  // Read the file as plain text (Markdown)
}

// Function to handle the drop event for Data files
function handleDataDrop(event) {
    event.preventDefault();
    const file = event.dataTransfer.files[0];
    const reader = new FileReader();

    reader.onload = function (e) {
        const markdownData = e.target.result;  
        console.log(markdownData);   
 
        fetch('http://127.0.0.1:5000/data', {
            method: 'POST',
            headers: {
                'Content-Type': 'text/plain',  
            },
            body: markdownData,  
        })
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json(); 
        })
        .then(responseData => {
            console.log('Received JSON:', responseData);

             
            currPart = 1
            numOfParts = responseData.num_of_parts; 
            const { data } = responseData; 
            console.log(`Number of parts: ${numOfParts}`);

            // restart the flags since a new document is dropped 
            isMarkDownDroped = new Array(numOfParts + 1).fill(false);;
            isDataDroped = true 
            
            // for window handling
            openedWindow = new Array(numOfParts + 1).fill(null);   
            
            openedNodesState = Array.from({ length: numOfParts + 1 }, () => ({}));
            openedNodesState[currPart] = getNodesStatus(data);
            console.log(openedNodesState); 
 
            d3.select("svg").remove(); 
            
            drawTree(data);
 
            const dropdown = document.getElementById("parts-dropdown");
            dropdown.innerHTML = ""; // Clear any existing options

            // Add options based on numOfParts
            for (let i = 1; i <= numOfParts; i++) {
                const option = document.createElement("option");
                option.value = `${i}`;
                option.textContent = `Part ${i}`;
                dropdown.appendChild(option);
            }
            
            dropdown.addEventListener("change", handlePartSelection);
 
            // Hide the drop area after successful upload
            const dropZone = document.getElementById('drop-zone-data');
            dropZone.style.display = 'none';   
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred while processing the file.');
        });
    };

    reader.readAsText(file);  // Read the file as plain text (Markdown)
}

// Function to handle part selection 
function handlePartSelection(event) {
    const selectedPart = event.target.value;  
 
    fetch('http://127.0.0.1:5000/parts', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ part_number: selectedPart }), 
        })
        .then(response => response.json())  
        .then(jsonData => {
        console.log('Received JSON:', jsonData);  
 
        currPart = jsonData.curr_part;
        console.log("Current part:", currPart);   

        const { data } = jsonData; 
        if (Object.keys(openedNodesState[currPart]).length === 0) { // if currPart nodes states not updated
            openedNodesState[currPart] = getNodesStatus(data);
        }

        
        d3.select("svg").remove();

        
        drawTree(jsonData.data); 

         
        // Show the download button
        const download = document.getElementById('download-btn');
        const dropZone = document.getElementById('drop-zone-md');
        if (isMarkDownDroped[currPart]) { 
            dropZone.style.display = 'none';  
            download.style.display = 'flex';  
        }
        else {  
            dropZone.style.display = 'flex';  
            dropZone.style.justifyContent = 'center';  
            dropZone.style.alignItems = 'center'; 
            download.style.display = 'none';  
        }
    })
    .catch(error => console.error('Error:', error));
}

// Function to handle generating heading for a node 
function generate_heading(node_name) { 
    if (!isMarkDownDroped[currPart]) {
        alert("Unable to generate node heading. Content is missing.");
        return; 
    } 

    // Show loading animation before the request
    const loading = document.getElementById("loading");
    loading.style.display = "flex";
 
    fetch('http://127.0.0.1:5000/node_heading', { 
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ 
            node_name: node_name 
        }) 
    }) 
    .then(response => response.json()) 
    .then(jsonData => {
        console.log('Received JSON:', jsonData);

        
        d3.select("svg").remove();

        
        drawTree(jsonData);
    })
    .catch(error => {
        console.error('Error:', error);
    }) 
    .finally(() => {
        loading.style.display = "none";
    });
}

 
// Attach the event listeners to the drop zones
document.getElementById('drop-zone-md').addEventListener('drop', handleMdDrop);
document.getElementById('drop-zone-data').addEventListener('drop', handleDataDrop);

// Prevent default behavior when dragging over the drop zones
document.getElementById('drop-zone-md').addEventListener('dragover', handleDragOver);
document.getElementById('drop-zone-data').addEventListener('dragover', handleDragOver);

// Function to allow the file to be dragged over
function handleDragOver(event) {
    event.preventDefault();
}

// a flag that states when the user right click on a node
let contextMenuActive = false;
   
// headings
document.getElementById("button").addEventListener("click", () => { 
    if (!isMarkDownDroped[currPart] || !isDataDroped) { 
        return; 
    } 

    fetch('http://127.0.0.1:5000/headings', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
    })
    .then(jsonData => {  
        console.log('Received JSON:', jsonData);  
        parseJsonData(jsonData);  
    
        
        d3.select("svg").remove();
    
        
        drawTree(jsonData);
    })
    .catch(error => {
        console.error('Error:', error);  
    });
});

// headings 
document.getElementById("button").addEventListener("click", () => { 
    if (!isDataDroped) {
        alert("No file dropped.");
        return;
    }
    if (!isMarkDownDroped[currPart]) {
        alert("Unable to generate headings. Content is missing.");
        return; 
    } 

    const loading = document.getElementById("loading");
    loading.style.display = "flex"; // Show the loading logo
    
    fetch('http://127.0.0.1:5000/titles', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
    })
        .then(response => { 
            if (!response.ok) {
                loading.style.display = "none"; // Hide loading logo if there's an error
                return response.json().then(data => { 
                    alert(data.error || "An error occurred.");
                });
            }
            return response.json();
        })
        .then(data => {
            if (response.ok) {
                console.log("Headers generated:", data);
                alert("Headers generated successfully!");
            }
        })
        .catch(error => {
            if (response.ok) {
                console.error("Error:", error);
                alert("An error occurred while generating headers.");
            }
        })
        .finally(() => { 
            loading.style.display = "none";
        });
});

// downloading the md file
document.getElementById("download-btn").addEventListener("click", function () {
    let filePath = `../Inputs/input${currPart}.md`; 
    window.open(filePath, "_blank");
});
 

// Function to process the JSON data (example)
function parseJsonData(jsonData) { 
    console.log('Parsing JSON data:', jsonData); 
}
 
// Function to create the tree diagram from the JSON data
function drawTree(treeData) {
    function getWidthOfText(txt, fontname, fontsize){
        if(getWidthOfText.c === undefined){
            getWidthOfText.c=document.createElement('canvas');
            getWidthOfText.ctx=getWidthOfText.c.getContext('2d');
        }
        var fontspec = fontsize + ' ' + fontname;
        if(getWidthOfText.ctx.font !== fontspec)
            getWidthOfText.ctx.font = fontspec;
        return getWidthOfText.ctx.measureText(txt).width;
    } 

    var root = d3.hierarchy(treeData, function(d) { return d.children; });
    var nodes = root.descendants();  
    
    
    function countOpenedNodes(node) {
        if (!node.children) return 1;  
        let count = 1; 
        for (const index in node.children) {  
            count += countOpenedNodes(node.children[index]);  
        }
        return count;
    }
 

    var openedNodesCount = countOpenedNodes(root); 
    const node_height = 25;
    const node_width = 200; 
     
    var margin = { top: openedNodesCount*(node_height/2), right: 90, bottom: 30, left: 90 },
        width = 4000 - margin.left - margin.right,  
        height =  openedNodesCount*node_height; 
 
    var treemap = d3.tree().nodeSize([node_height, node_width]);
   
 
    var svg = d3.select("body")
        .append("svg")
        .attr("width", width + margin.right + margin.left)
        .attr("height", height + margin.top + margin.bottom)  
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
 
    var i = 0, duration = 300, root; 

    root = d3.hierarchy(treeData, function (d) { return d.children; }); 
    root.x0 = 0;
    root.y0 = 0;

    if (root.children) {
        root.children.forEach(collapse);
    }  

    update(root);
    
    function collapse(d) {
        const section = d.data.name.split(" ")[0];    
        if (openedNodesState[currPart][section] === false) {
            // Collapse this node
            if (d.children) {
                d._children = d.children;   
                d.children = null;  
                d._children.forEach(collapse);
            }
        } else if (openedNodesState[currPart][section] === true) {
            // Expand this node
            if (d._children) {
                d.children = d._children;  
                d._children = null;   
                d.children.forEach(collapse);
            }
        }
     
        if (d.children) {
            d.children.forEach(collapse);
        }
    }
    
     
    window.scrollTo({
        top: (openedNodesCount*(node_height/2) - 350),  // Scroll to the tree
        behavior: 'smooth' 
    });


    function update(source) {  
        var treeData = treemap(root);

        var nodes = treeData.descendants(),
            links = treeData.descendants().slice(1);  

        let maxWidthsByDepth = {}; 
 
        // Calculate the maximum text width for each depth
        nodes.forEach(function (d) {
            const textWidth = getWidthOfText(d.data.name, "sans-serif", "12px");
            if (!maxWidthsByDepth[d.depth] || maxWidthsByDepth[d.depth] < textWidth) {
                maxWidthsByDepth[d.depth] = textWidth;
            }
        });

        // Update each node's y-position based on the maximum width for its depth
        nodes.forEach(function (d) {
            let totalWidth = 0;
            let current = d;

            while (current) {
                if (current.depth >= 1)
                    totalWidth += 100 + maxWidthsByDepth[current.depth] + 12; 
                else
                    totalWidth += maxWidthsByDepth[current.depth] + 12; 
                current = current.parent;
            }

            d.y = totalWidth;
        });


        var node = svg.selectAll('g.node') 
            .data(nodes, function (d) { return d.id || (d.id = ++i); });

            var nodeEnter = node.enter().append('g')
            .attr('class', 'node')
            .attr("transform", function (d) {
                return "translate(" + source.y0 + "," + source.x0 + ")";
            }) 
            .on('click', click) 
            .on('mouseover', function() {
                // Change the cursor to a pointer on hover
                d3.select(this).style('cursor', 'pointer');
            })
            .on('mouseout', function() {
                // Revert back to the default cursor
                d3.select(this).style('cursor', 'default');
            })
            .on('contextmenu', function(d) {
                contextMenuActive = true;

                event.preventDefault(); // Prevent the default right-click menu 
                let section = d.data.name.split(" ")[0]; 

                let buttonGroup = d3.select(this).append("g")
                    .attr("class", "context-menu-button")
                    .attr("transform", "translate(0, -30)"); // Position it above the node
   
                // Create a background rectangle for the button
                buttonGroup.append("rect")
                    .attr("width", 120)
                    .attr("height", d.data.color != "white" ? 60 : 30)
                    .attr("x", -60)  
                    .attr("y", -15)
                    .attr("rx", 5)  
                    .attr("fill", "white")  
                    .style("opacity", 0.9);
            
                // Create the button text for "Show Content"
                buttonGroup.append("text")
                    .attr("class", "button-text")
                    .attr("x", 0)
                    .attr("y", 4)
                    .attr("text-anchor", "middle")
                    .style("fill", "black")
                    .style("cursor", "pointer")
                    .text("Show Content")
                    .on("click", function() {
                        if (!openedWindow[currPart] || openedWindow[currPart].closed) {
                            // If the window isn't open or has been closed, open it
                            openedWindow[currPart] = window.open(`../Outputs/content.html#${section}`);
                        } else {
                            // If the window is open, focus on it
                            openedWindow[currPart].location.href = `../Outputs/content.html#${section}`;
                            openedWindow[currPart].focus();
                        }
                    }); 

                    // Create the button text for "generate heading"
                    if (d.data.color != "white") {
                        buttonGroup.append("text")
                        .attr("class", "button-text")
                        .attr("x", 0)
                        .attr("y", 33)
                        .attr("text-anchor", "middle")
                        .style("fill", "black")
                        .style("cursor", "pointer")
                        .text("Generate Heading")
                        .on("click", function() { 
                            generate_heading(d.data.name);
                        });
                    }
         
                d3.select("body").on("click", function() {
                    d3.select(".context-menu-button").remove(); 
                    contextMenuActive = false; 
                });
            });


        nodeEnter.append('circle')
            .attr("r", 7) 
            .style("fill", function(d) {
                return d.data.fill !== 'none' ? d.data.fill : "none"; 
            })
            .style("stroke", function(d) {
                return d.data.fill !== 'none' ? "#6A7F8C" : "none"; 
            })
            .style("stroke-width", 2) 
            

        nodeEnter.append('text')
            .attr("dx", function (d) {
                return -getWidthOfText(d.data.name, "Arial", "12px")/2 - 12;  
            })
            .attr("dy", -2)
            .attr("text-anchor", "middle")
            .style("fill", function(d) {return d.data.color}) 
            .text(function (d) { return d.data.name; })
            .each(function(d) {
                var textWidth = this.getBBox().width;
                d.textWidth = textWidth;
            });

        var nodeUpdate = nodeEnter.merge(node);

        nodeUpdate.transition()
            .duration(duration)
            .attr("transform", function (d) {
                return "translate(" + d.y + "," + d.x + ")";
            });

        var nodeExit = node.exit().transition()
            .duration(duration)
            .attr("transform", function (d) {
                return "translate(" + source.y + "," + source.x + ")";
            })
            .remove();

        var link = svg.selectAll('path.link')
            .data(links, function (d) { return d.id; });

        var linkEnter = link.enter().insert('path', "g")
            .attr("class", "link")
            .attr('d', function (d) {
                var o = { x: source.x0, y: source.y0 };
                return diagonal(o, o);
            })
            .style("stroke-width", 2)
            .style("stroke", function(d) {return "white"});


        var linkUpdate = linkEnter.merge(link);

        linkUpdate.transition()
            .duration(duration)
            .attr('d', function (d) { return diagonal(d, d.parent); });

        var linkExit = link.exit().transition()
            .duration(duration)
            .attr('d', function (d) {
                var o = { x: source.x, y: source.y };
                return diagonal(o, o);
            })
            .remove();

        nodes.forEach(function (d) {
            d.x0 = d.x;
            d.y0 = d.y;
        });

        function curveLine(s, d) {
            const curvature = 0.5; 
            const hx1 = s.y + (d.y - s.y) * curvature;
            const hx2 = d.y - (d.y - s.y) * curvature;
        
            return `M ${s.y} ${s.x} 
                    C ${hx1} ${s.x}, ${hx2} ${d.x}, ${d.y} ${d.x}`;
        }

        function straightLine(s, d) {
            return `M ${s.y} ${s.x} L ${d.y} ${d.x}`; 
        }

        function diagonal(s, d) {
            q = { ...s };  
            q.y = d.y + 100;
            const curve = curveLine(q, d); 
            const line = straightLine(s, q); 
            return curve + line; 
        }

        function click(d) {
            const section = d.data.name.split(" ")[0]
            if (!contextMenuActive) {
                openedNodesState[currPart][section] = !openedNodesState[currPart][section];  
            }
            console.log(openedNodesState)  
            if (!contextMenuActive) {
                if (d.children) {
                    d._children = d.children;
                    d.children = null;
                } else {
                    d.children = d._children;
                    d._children = null;
                }
                update(d); 
            }
        } 
    }
} 

// Function to handle the drop event for Markdown files
function handleMdDrop(event) {
    event.preventDefault();
    const file = event.dataTransfer.files[0];
    const reader = new FileReader();

    reader.onload = function (e) {
        const markdownData = e.target.result;  // Read as plain text
        console.log(markdownData);  // Log the content of the Markdown file

        // Make an API call to send the Markdown data
        fetch('http://127.0.0.1:5000/markdown', {
            method: 'POST',
            headers: {
                'Content-Type': 'text/plain',  // Content type is plain text now
            },
            body: markdownData,  // Send the raw Markdown content
        })
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();  // Parse the JSON response
        })
        .then(jsonData => {
            console.log('Received JSON:', jsonData);  // Log the JSON data
            parseJsonData(jsonData);  // Process the JSON data (if necessary)
        
            // Ensure any existing tree is removed before drawing a new one
            d3.select("svg").remove();
        
            // Draw the tree with the analyzed JSON data
            drawTree(jsonData);
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred while processing the file.');
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
        const markdownData = e.target.result;  // Read as plain text
        console.log(markdownData);  // Log the content of the Markdown file

        // Make an API call to send the Markdown data
        fetch('http://127.0.0.1:5000/data', {
            method: 'POST',
            headers: {
                'Content-Type': 'text/plain',  // Content type is plain text now
            },
            body: markdownData,  // Send the raw Markdown content
        })
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();  // Parse the JSON response
        })
        .then(responseData => {
            console.log('Received JSON:', responseData);

            const { num_of_parts, data } = responseData;

            // Display the number of parts if needed
            console.log(`Number of parts: ${num_of_parts}`);

            // Ensure any existing tree is removed before drawing a new one
            d3.select("svg").remove();

            // Draw the tree with the analyzed JSON data
            drawTree(data);

            // Dynamically update the dropdown with the number of parts from response
            const dropdown = document.getElementById("parts-dropdown");
            dropdown.innerHTML = ""; // Clear any existing options

            // Add options based on num_of_parts
            for (let i = 1; i <= num_of_parts; i++) {
                const option = document.createElement("option");
                option.value = `${i}`;
                option.textContent = `Part ${i}`;
                dropdown.appendChild(option);
            }
            
            dropdown.addEventListener("change", handlePartSelection);
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
    const selectedPart = event.target.value;  // Get the selected part number

    // Send the selected part to the backend
    fetch('http://127.0.0.1:5000/parts', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ part_number: selectedPart }), // Send the part number in the body
    })
    .then(response => response.json()) // Parse the response as JSON
    .then(jsonData => {
        console.log('Received JSON:', jsonData);  // Log the JSON data

        // Ensure any existing tree is removed before drawing a new one
        d3.select("svg").remove();

        // Draw the tree with the analyzed JSON data
        drawTree(jsonData);
    })
    .catch(error => console.error('Error:', error));
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

let openedNodesState = { 
    // "3 Terms, definitions and abbreviations": true, 
    // "4 Requirements for the safety of software in relation to the intended function": true, 
    // "5 Software management and organisation": true, 
    // "6 Software assurance": true, 
    // "7 Generic software development": true, 
    // "8 Development of application data or algorithms: systems configured by application data or algorithms": true, 
    // "9 Software deployment and maintenance": true
};  // This will store the open/close state of nodes



function generate_heading(name) { 
    console.log(name); // Print the name to the console

    // Send a request to the backend
    fetch('http://127.0.0.1:5000/node_title', { // Update with your actual backend URL
        method: 'POST',
        headers: {
            'Content-Type': 'application/json' // Sending JSON data
        },
        body: JSON.stringify({ name: name }) // Send the name in the request body
    }) 
    .then(response => response.json()) // Parse the response as JSON
    .then(jsonData => {
        console.log('Received JSON:', jsonData);  // Log the JSON data

        // Ensure any existing tree is removed before drawing a new one
        d3.select("svg").remove();

        // Draw the tree with the analyzed JSON data
        drawTree(jsonData);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}



document.getElementById("button").addEventListener("click", () => {
    fetch('http://127.0.0.1:5000/titles', {
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
        console.log('Received JSON:', jsonData);  // Log the JSON data
        parseJsonData(jsonData);  // Process the JSON data (if necessary)
    
        // Ensure any existing tree is removed before drawing a new one
        d3.select("svg").remove();
    
        // Draw the tree with the analyzed JSON data
        drawTree(jsonData);
    })
    .catch(error => {
        console.error('Error:', error);  // Log any errors
    });
});


document.getElementById("button").addEventListener("click", () => {
    const loading = document.getElementById("loading");
    loading.style.display = "block"; // Show the loading logo
    
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
            // Loading should already be hidden in error cases, but ensure it's hidden
            loading.style.display = "none";
        });
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
    var nodes = root.descendants(); // Now you can call descendants on the root
    
    // console.log("Number of opened nodes:", nodes.filter(node => node.children).length);

    
    function countOpenedNodes(node) {
        if (!node.children) return 1;  
        let count = 1; 
        for (const index in node.children) {  
            count += countOpenedNodes(node.children[index]); 
            console.log(count)
        }
        return count;
    }

    var treeDepth = d3.max(nodes, function(d) { return d.depth; });
     
    var margin = { top: 2000, right: 90, bottom: 30, left: 90 },
        width = 4000 - margin.left - margin.right,  
        // height = countOpenedNodes(root) * 0.5; 
        height =  window.innerHeight * 20; 


    // var treemap = d3.tree().size([height, width]);
    var treemap = d3.tree().nodeSize([25, 200]);
   

    var svg = d3.select("body").append("svg")
        .attr("width", width + margin.right + margin.left)
        .attr("height", height + margin.top + margin.bottom) // Set dynamic height
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");


    var i = 0, duration = 300, root; 

    root = d3.hierarchy(treeData, function (d) { return d.children; });
    root.x0 = height / 2;
    root.y0 = 0;

    root.children.forEach(collapse);
    // root.collapse;

    update(root);

    
    function collapse(d) {
        if (d.children && openedNodesState[d.data.name] !== undefined) {
        // if (d.children ) {
            console.log(d.data.name)
            d._children = d.children;
            d._children.forEach(collapse);
            d.children = null;
        }
    }


    function update(source) {  
        var treeData = treemap(root);

        var nodes = treeData.descendants(),
            links = treeData.descendants().slice(1); 
            
        var openedNodesCount = countOpenedNodes(root); 

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
                    .attr("x", -60) // Center it horizontally
                    .attr("y", -15)
                    .attr("rx", 5) // Rounded corners
                    .attr("fill", "white") // Background color
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
                        window.open(`C:/Users/Ameer Tabri/Desktop/LLM/z.html#${section}`);
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
        
            
                // Add an event to remove the context menu if the user clicks anywhere else on the screen
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
            if (contextMenuActive === false) {
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

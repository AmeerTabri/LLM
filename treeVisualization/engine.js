// Function to handle the drop event for Markdown files
function handleMdDrop(event) {
    event.preventDefault();
    const file = event.dataTransfer.files[0];
    const reader = new FileReader();

    reader.onload = function (e) {
        const markdownData = e.target.result;  // Read as plain text
        console.log(markdownData);  // Log the content of the Markdown file

        // Make an API call to send the Markdown data
        fetch('http://127.0.0.1:5000/analyze', {
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
        const data = e.target.result;  // Read as plain text
        console.log(data);  // Log the content of the Data file

        // Make an API call to send the Data file
        fetch('http://127.0.0.1:5000/data', {
            method: 'POST',
            headers: {
                'Content-Type': 'text/plain',  // Content type is plain text now
            },
            body: data,  // Send the raw Data content
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

    reader.readAsText(file);  // Read the file as plain text (Data)
}

// Attach the event listeners to the drop zones
document.getElementById('drop-zone-md').addEventListener('drop', handleMdDrop);
document.getElementById('drop-zone-data').addEventListener('drop', handleDataDrop);

// Prevent default behavior when dragging over the drop zones (to allow dropping)
document.getElementById('drop-zone-md').addEventListener('dragover', function(event) {
    event.preventDefault();
});
document.getElementById('drop-zone-data').addEventListener('dragover', function(event) {
    event.preventDefault();
});


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

// Function to allow the file to be dragged over
function handleDragOver(event) {
    event.preventDefault();
}

// Set up the drag-and-drop area
const dropZone = document.getElementById("drop-zone");
dropZone.addEventListener("dragover", handleDragOver);
dropZone.addEventListener("drop", handleDrop);

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


    var treeDepth = d3.max(nodes, function(d) { return d.depth; });
     
    var margin = { top: 20, right: 90, bottom: 30, left: 90 },
        width = 4000 - margin.left - margin.right,  
        // height = countOpenedNodes(root) * 12; 
        height =  window.innerHeight*.7; 

    var treemap = d3.tree().size([height, width]);
   
    var svg = d3.select("body").append("svg")
        .attr("width", width + margin.right + margin.left)
        .attr("height", height + margin.top + margin.bottom)
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
        if (d.children) {
            d._children = d.children;
            d._children.forEach(collapse);
            d.children = null;
        }
    }

    function countOpenedNodes(node) {
        if (!node.children) return 1;  
        let count = 1; 
        for (const index in node.children) {  
            count += countOpenedNodes(node.children[index]); 
            console.log(count)
        }
        return count;
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
            .on('contextmenu', function (event, d) { 
                let section = 8;
                window.open(`C:/Users/Ameer Tabri/Desktop/LLM/z.html#${section}`);

                console.log("Left-clicked on node:"); 
            });

        nodeEnter.append('circle')
            .attr("r", 7) 
            .style("fill", function(d) {
                return d.data.fill !== 'none' ? d.data.fill : "none"; 
            })
            .style("stroke", function(d) {
                return d.data.fill !== 'none' ? "#6A7F8C" : "none"; 
            })
            .style("stroke-width", 2); 

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

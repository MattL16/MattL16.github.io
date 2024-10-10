// Embed the choropleth map
var vg_1 = "unemployment_rate_V2.json";
vegaEmbed("#choropleth_map", vg_1, {
    scaleFactor: 2,    // Increase scale for better quality
    renderer: 'svg'    // Use SVG rendering for sharper results
}).then(function(result) {
    // Access the Vega view instance if needed
}).catch(console.error);

// Embed the line chart (new chart)
var vg_2 = "linechart.json";
vegaEmbed("#line_chart", vg_2, {
    scaleFactor: 2,    // Increase scale for better quality
    renderer: 'svg'    // Use SVG rendering for sharper results
}).then(function(result) {
    // Access the Vega view instance for the line chart
}).catch(console.error);

// Embed the bar chart (new chart)
var vg_3 = "barchart.json";
vegaEmbed("#bar_chart", vg_3, {
    scaleFactor: 2,    // Increase scale for better quality
    renderer: 'svg'    // Use SVG rendering for sharper results
}).then(function(result) {
    // Access the Vega view instance for the bar chart
}).catch(console.error);

// Embed the bubble chart (new chart)
var vg_4 = "Bubblechart.json";
vegaEmbed("#bubble_chart", vg_4, {
    scaleFactor: 2,    // Increase scale for better quality
    renderer: 'svg'    // Use SVG rendering for sharper results
}).then(function(result) {
    // Access the Vega view instance for the bubble chart
}).catch(console.error);

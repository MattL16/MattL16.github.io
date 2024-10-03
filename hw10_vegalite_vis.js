// Embed the choropleth map
var vg_1 = "unemployment_rate.json";
vegaEmbed("#choropleth_map", vg_1).then(function(result) {
    // Access the Vega view instance if needed
}).catch(console.error);

// Embed the line chart (new chart)
var vg_2 = "linechart.json";
vegaEmbed("#line_chart", vg_2).then(function(result) {
    // Access the Vega view instance for the line chart
}).catch(console.error);
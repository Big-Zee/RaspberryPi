/*JSC.Chart('chartDiv', {
    type: 'horizontal column',
    series: [
       {
          name:'Andy',
          points: [
             {x: 'Apples', y: 50},
             {x: 'Oranges', y: 32}
          ]
       },{
          name:'Anna',
          points: [
             {x: 'Apples', y: 30},
             {x: 'Oranges', y: 22}
          ]
       }
    ]
 });
*/
//var json = require('./AirState.csv');
//console.log(json);

/*
var fs = require("fs"); 
var text = fs.readFileSync("./​mytext.txt"); 
//var textByLine = text.split("\n").
console.log(text);*/


fetch('http://192.168.0.118/AirState.csv')
   .then(function (response) {
       console.log(response.text);
      return response.text();
   })
   .then(function (text) {
    let series = csvToSeries(text);
	//renderChart(series);
   })
   .catch(function (error) {
      //Something went wrong
      console.log(error);
   });

   function csvToSeries(text) {
	const lifeExp = 'average_life_expectancy';
	let dataAsJson = JSC.csv2Json(text);
    console.log(dataAsJson);
	/*let male = [], female = [];
	dataAsJson.forEach(function (row) {
		 //add either to male, female, or discard.
		if (row.race === 'All Races') {
			if (row.sex === 'Male') {
				male.push({x: row.year, y: row[lifeExp]});
			} else if (row.sex === 'Female') {
				female.push({x: row.year, y: row[lifeExp]});
			}
		}
	});
    console.log([male, female]);
    return [
        {name: 'Male', points: male},
        {name: 'Female', points: female}
     ];*/
}

function renderChart(series){
	JSC.Chart('chartDiv', {
		title_label_text: 'Life Expectancy in the United States',
		annotations: [{
			label_text: 'Source: National Center for Health Statistics',
			position: 'bottom left'
		}],
        legend_visible: false,
		defaultSeries_lastPoint_label_text: '<b>%seriesName</b>',
		defaultPoint_tooltip: '%seriesName <b>%yValue</b> years',
		xAxis_crosshair_enabled: true,
		series: series
	});
}
function parseData(creategraph){
	var rightNow = new Date();
	var res = rightNow.toISOString().slice(0,10).replace(/-/g,"");
	Papa.parse("../static/logs/" + res + ".csv",{
		download: true,
		complete: function(results){
			createGraph(results.data);
		}
	});
}

function createGraph(data){
	var temp0 = ["RPI Enclosure Temp"];
	var temp1 = ["NTC 2"];
	var temp2 = ["NTC 3"];
	var temp3 = ["NTC 4"];
	var cputemp = ["RPI CPU Temp"];
	var time = [];

	for (var i = 1; i < data.length -1; i++){
		time.push(data[i][3]+":"+data[i][4]+":"+data[i][5]+" "+data[i][2]+"-"+data[i][1]+"-"+data[i][0]);
		temp0.push(data[i][6]);
		temp1.push(data[i][7]);
		temp2.push(data[i][8]);
		temp3.push(data[i][9]);
		cputemp.push(data[i][10]);
	}
	console.log(time);
	console.log(temp0);
	
	var chart = c3.generate({
		bindto: '#chart',
	    	data: {
			columns: [temp1,temp2,temp3,temp0,cputemp],
			type: 'spline',
			hide: true,
			hide: ['temp0',temp0,cputemp],
		},
		axis: {
		        x: {
				show: false,
				type: 'category',
				categories: time
		        },
			y: {
				tick:{
					format: d3.format(",.1f")
				},
				label: 'Deg C'
			}
    		},
		zoom: {
			enabled: true
	    	},
		grid: {
			y: {
			    show: true
			},
		}
		
	});
	}
	
parseData (createGraph);

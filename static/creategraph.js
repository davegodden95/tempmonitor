function parseData(creategraph){
	Papa.parse("../static/data.csv",{
		download: true,
		complete: function(results){
			createGraph(results.data);
		}
	});
}

function createGraph(data){
	var temp0 = ["NTC 1"];
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
			columns: [temp0,temp1,temp2,temp3,cputemp]
		},
		axis: {
		        x: {
		            type: 'category',
		            categories: time
		        }
    		},
		zoom: {
			enabled: true
	    	}
		
	});
	}
	
parseData (createGraph);

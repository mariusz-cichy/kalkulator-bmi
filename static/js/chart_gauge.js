var chart = c3.generate({
    data: {
        columns: [
            ['BMI', 24.2]
        ],
        type: 'gauge',
        onclick: function (d, i) { console.log("onclick", d, i); },
        onmouseover: function (d, i) { console.log("onmouseover", d, i); },
        onmouseout: function (d, i) { console.log("onmouseout", d, i); }
    },
    gauge: {
        label: {
           format: function(value, ratio) {
               return value;
           },
           show: false // to turn off the min/max labels.
        },
        max: 40
        //    min: 0, // 0 is default, //can handle negative min e.g. vacuum / voltage / current flow / rate of change
//    max: 100, // 100 is default
//    units: ' %',
//    width: 39 // for adjusting arc thickness

    },
    color: {
        pattern: ['#3498DB', '#27AE60', '#FFC300', '#C70039'], // the three color levels for the percentage values.
        threshold: {
            unit: 'value', // percentage is default
//            max: 200, // 100 is default
//             min: 0,
            max: 40,
            values: [18.4, 25, 30, 40]
            // values: [30, 60, 90, 100]
        }
    },
    size: {
        height: 200
    },
    legend: {
        hide: true
    }
 });

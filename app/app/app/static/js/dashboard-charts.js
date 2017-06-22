var ctx = $("#temperature")[0].getContext('2d');
var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ["", "", "", "", "", ""],
        datasets: [{
            label: 'Temperature',
            data: tempdata,
            borderWidth: 1
        }]
    },
});

var ctx2 = $("#pressure")[0].getContext('2d');
var myChart = new Chart(ctx2, {
    type: 'line',
    data: {
        labels: ["", "", "", "", "", ""],
        datasets: [{
            label: 'Pressure',
            data: presdata,
            borderWidth: 1
        }]
    },
    options: {
    }
});

var ctx3 = $("#humidity")[0].getContext('2d');
var myChart = new Chart(ctx3, {
    type: 'line',
    data: {
        labels: ["", "", "", "", "", ""],
        datasets: [{
            label: 'Humidity',
            data: humdata,
            borderWidth: 1
        }]
    },
    options: {
    }
});

var ctx4 = $("#co2")[0].getContext('2d');
var myChart = new Chart(ctx4, {
    type: 'line',
    data: {
        labels: ["", "", "", "", "", ""],
        datasets: [{
            label: 'Co2',
            data: co2data,
            borderWidth: 1
        }]
    },
    options: {
    }
});

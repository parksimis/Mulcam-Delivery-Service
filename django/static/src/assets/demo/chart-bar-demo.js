// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Bar Chart Example

var ctx = document.getElementById("main_line");
var main_line_lbl = $('#main_line_lbl').val();
var main_line_val = $('#main_line_val').val();

var main_lbl = main_line_lbl.replaceAll('[', '').replaceAll(']', '').replaceAll(',', '').replaceAll("'", '')
var main_val = main_line_val.replaceAll('[', '').replaceAll(']', '').replaceAll(',', '')

var main_lbl_final = main_lbl.split(' ')
var main_val_final = main_val.split(' ')

var myLineChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: main_lbl_final,
    datasets: [{
      label: "일자별 평균 주문예측건수",
      lineTension: 0.3,
      backgroundColor: "rgba(218,241,223,0.4)",
      borderColor: "rgba(95,196,118,1)",
      pointRadius: 6,
      pointBackgroundColor: "rgba(255,255,255,1)",
      pointBorderColor: "rgba(95,196,118,1)",
      pointHoverRadius: 5,
      pointHoverBackgroundColor: "rgba(90,194,114,0.9)",
      pointHitRadius: 50,
      pointBorderWidth: 3,
      data: main_val_final,
    }],
  },
  options: {
    scales: {
      xAxes: [{
        time: {
          unit: 'date'
        },
        gridLines: {
          display: true
        },
        ticks: {
          maxTicksLimit: 31
        }
      }],
      yAxes: [{
        ticks: {
          min: 0,
          max: 150000,
          maxTicksLimit: 10
        },
        gridLines: {
          color: "rgba(0, 0, 0, .125)",
        }
      }],
    },
    legend: {
      display: false
    }
  }
});

// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Pie Chart Example
var ctx = document.getElementById("main_pie");

var main_pie_lbl = $('#main_pie_lbl').val();
var main_pie_val = $('#main_pie_val').val();

var pie_lbl = main_pie_lbl.replaceAll('[', '').replaceAll(']', '').replaceAll(',', '').replaceAll("'", '')
var pie_val = main_pie_val.replaceAll('[', '').replaceAll(']', '').replaceAll(',', '').replaceAll('.  ', '.00 ').replaceAll('   ', ' ').replaceAll('  ', ' ')

var pie_lbl_final = pie_lbl.split(' ')
var pie_val_final = pie_val.split(' ')

var myPieChart = new Chart(ctx, {
  type: 'pie',
  data: {
    labels: pie_lbl_final,
    datasets: [{
      data: pie_val_final,
      backgroundColor: ['#037F8C', '#205459', '#F2E7C4', '#F28F38', '#F25757', '#03738C', '#04BFAD', '#D9CE36',
      '#F2E8B6','#F26B6B' ,'#153259'],
    }],
  },
});



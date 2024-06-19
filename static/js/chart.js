new Chart("myChart", {
  type: "doughnut",
  data: {
    labels: xValues,
    datasets: [{
      backgroundColor: barColors,
      data: yValues,
      borderRadius: 10, // Adjust this value to make edges rounder
    }]
  },
  options: {
    title: {
      display: true,
      text: "Cleaning Activities"
    },
    cutoutPercentage: 70, // Adjust this value to change the thickness of the doughnut
    rotation: -0.5 * Math.PI, // This will rotate the chart to start from the top
    circumference: 2 * Math.PI, // This will make the chart a full circle
  }
});

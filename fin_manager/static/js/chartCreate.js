document.addEventListener('DOMContentLoaded', function () {
    const canvas = document.getElementById('financeChart');
    const ctx = canvas.getContext('2d');

    const income = parseFloat(canvas.dataset.income);
    const expenses = parseFloat(canvas.dataset.expenses);

    const financeChart = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: ['Income', 'Expenses'],
            datasets: [{
                label: 'Amount ($)',
                data: [income, expenses],
                backgroundColor: ['#107D57', '#072E42'],
                borderColor: ['#083d2b', '#03141c'],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: { beginAtZero: true }
            }
        }
    });
});

$(function () {
    var chart = c3.generate({
        bindto: '#chart',

        data: {
            columns: [
                ['Stat', 30, 200, 100, 400, 150, 250]
            ]
        }
    });
});

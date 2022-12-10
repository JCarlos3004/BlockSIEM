$(function() {

    Morris.Area({
        element: 'morris-area-chart',
        data: [{
            period: '2022, 1 Dic',
            critico: 32,
            enespera: 30,
            nocritico: 40
        }, {
            period: '2022, 1 Dic',
            critico: 29,
            enespera: 31,
            nocritico: 14
        }, {
            period: '2022, 1 Dic',
            critico: 51,
            enespera: 15,
            nocritico: 27
        }, {
            period: '2022, 1 Dic',
            critico: 41,
            enespera: 37,
            nocritico: 18
        }, {
            period: '2022, 2 Dic',
            critico: 37,
            enespera: 50,
            nocritico: 41
        }, {
            period: '2022, 2 Dic',
            critico: 54,
            enespera: 13,
            nocritico: 16
        }, {
            period: '2022, 2 Dic',
            critico: 71,
            enespera: 19,
            nocritico: 26
        }, {
            period: '2022, 2 Dic',
            critico: 31,
            enespera: 47,
            nocritico: 40
        }, {
            period: '2022, 3 Dic',
            critico: 43,
            enespera: 21,
            nocritico: 31
        }, {
            period: '2022, 3 Dic',
            critico: 67,
            enespera: 57,
            nocritico: 14
        }],
        xkey: 'period',
        ykeys: ['critico', 'nocritico','enespera'],
        labels: ['critico', 'nocritico','enespera'],
        pointSize: 2,
        hideHover: 'auto',
        resize: true
    });

    Morris.Donut({
        element: 'morris-donut-chart',
        data: [{
            label: "Logs Red",
            value: 400
        }, {
            label: "En espera de veficicación",
            value: 200
        }, {
            label: "Logs Kernel",
            value: 420
        }],
        resize: true
    });

    Morris.Bar({
        element: 'morris-bar-chart',
        data: [{
            y: '1 Dic',
            a: 75,
            b: 65,
            c: 100
        }, {
            y: '2 Dic',
            a: 75,
            b: 65,
            c: 100
        }, {
            y: '3 Dic',
            a: 100,
            b: 90,
            c: 100
        }],
        xkey: 'y',
        ykeys: ['a', 'b','c'],
        labels: ['Criticos', 'No criticos','En espera'],
        hideHover: 'auto',
        resize: true
    });

});

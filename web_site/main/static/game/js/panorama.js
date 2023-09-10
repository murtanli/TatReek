var mas = [[54.325734, 48.360569],[54.273387, 48.266860],[55.756651, 48.751902], [54.267378, 48.323189], [55.870468, 48.551614],[54.325963, 48.375168]
[56.175415, 50.904331],[55.818490, 49.088179],[55.874082, 48.579938],[55.959684, 49.408220],[55.752335, 49.204111],[55.850266, 48.508604],
[54.372480, 48.596534],[56.429253, 50.758498],[55.799151,49.104882 ]]//3 не работают

ymaps.ready(function () {
    // Для начала проверим, поддерживает ли плеер браузер пользователя.
    if (!ymaps.panorama.isSupported()) {
        // Если нет, то просто ничего не будем делать.
        return;
    }
    
    // Ищем панораму в переданной точке.
    ymaps.panorama.locate(mas[13]).done(
        function (panoramas) {
            // Убеждаемся, что найдена хотя бы одна панорама.
            if (panoramas.length > 0) {
                // Создаем плеер с одной из полученных панорам.
                var player = new ymaps.panorama.Player(
                        'player1',
                        // Панорамы в ответе отсортированы по расстоянию
                        // от переданной в panorama.locate точки. Выбираем первую,
                        // она будет ближайшей.
                        panoramas[0],
                        {controls: [],
                        suppressMapOpenBlock: ['true'],
                    },
                        // Зададим направление взгляда, отличное от значения
                        // по умолчанию.
                        { direction: [256, 16] }
                    );
                    player.events.add(["panoramachange"], function (e) {
                        const panorama = player.getPanorama();
                        panorama.setMarkers([]) ;
                        player.setPanorama(panorama);
                    });

                
            }
        },
        function (error) {
            // Если что-то пошло не так, сообщим об этом пользователю.
            alert(error.message);
        }
    
    );

    // Для добавления панорамы на страницу также можно воспользоваться
    // методом panorama.createPlayer. Этот метод ищет ближайщую панораму и
    // в случае успеха создает плеер с найденной панорамой.
    
});

var myMap;

// Дождёмся загрузки API и готовности DOM.
ymaps.ready(init);

function init () {
    // Создание экземпляра карты и его привязка к контейнеру с
    // заданным id ("map").
    myMap = new ymaps.Map('map', {
        // При инициализации карты обязательно нужно указать
        // её центр и коэффициент масштабирования.
        center: [55.796129, 49.106414], // Москва
        zoom: 6
    }, {
        searchControlProvider: 'yandex#search'
    });

    // myMap.controls.remove('searchControl');
    // myMap.controls.remove('rulerControl');
    // myMap.controls.remove('trafficControl');
    // myMap.controls.remove('typeSelector');
    // myMap.controls.remove('geolocationControl');
    // myMap.controls.remove('fullscreenControl');
    // myMap.controls.remove('routePanelControl');
    // myMap.controls.remove('routeButtonControl');
    

    

}

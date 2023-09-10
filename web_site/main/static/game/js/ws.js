let countdown;

    function startTimer(seconds) {
        clearInterval(countdown); // Очищаем предыдущий таймер, если есть
        const timerDisplay = document.getElementById('timer');
        const startTime = Date.now();
        const endTime = startTime + (seconds * 1000);
        function displayTimeLeft() {
            const secondsLeft = Math.round((endTime - Date.now()) / 1000);
            if (secondsLeft < 0) {
                clearInterval(countdown);
                timerDisplay.textContent = 'Время вышло!';
                return;
            }
            const minutes = Math.floor(secondsLeft / 60);
            const remainingSeconds = secondsLeft % 60;
            const display = `${minutes}:${remainingSeconds < 10 ? '0' : ''}${remainingSeconds}`;
            timerDisplay.textContent = display;
        }
        displayTimeLeft(); // Первоначально отобразим оставшееся время
        countdown = setInterval(displayTimeLeft, 1000); // Обновляем отображение каждую секунду
    }
startTimer(20);
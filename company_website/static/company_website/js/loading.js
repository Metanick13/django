/* JavaScript для экрана загрузки (splash screen) */
document.addEventListener('DOMContentLoaded', function() {
    const loadingScreen = document.getElementById('loading-screen');
    const loadingPercentage = document.getElementById('loading-percentage');
    let progress = 0;

    // Устанавливаем интервал для обновления прогресса загрузки
    const interval = setInterval(() => {
        progress += 1; // Увеличиваем прогресс на 1% (для более плавной анимации)
        if (progress <= 100) {
            if (loadingPercentage) {
                loadingPercentage.textContent = progress + '% ';
            }
        } else {
            clearInterval(interval); // Останавливаем интервал, когда прогресс достигает 100%
        }
    }, 50); // Обновляем каждые 50мс для более плавной анимации

    // Событие window.load срабатывает, когда все ресурсы страницы загружены
    window.addEventListener('load', function() {
        // Убедимся, что прогресс достиг 100%, прежде чем скрывать экран
        progress = 100;
        if (loadingPercentage) {
            loadingPercentage.textContent = '100%';
        }
        if (loadingScreen) {
            loadingScreen.style.opacity = '0'; // Плавно скрываем экран загрузки
            // После завершения анимации скрытия, полностью удаляем элемент
            loadingScreen.addEventListener('transitionend', function() {
                loadingScreen.style.display = 'none';
            });
        }
    });

    // JavaScript для модального окна "Карта сайта"
    const openSitemapButton = document.getElementById('open-sitemap-modal');
    const sitemapModal = document.getElementById('sitemap-modal');
    const closeSitemapModal = document.querySelector('.close-modal');

    if (sitemapModal) {
        sitemapModal.style.display = 'none'; // Убедимся, что модальное окно скрыто по умолчанию
    }

    if (openSitemapButton) {
        openSitemapButton.addEventListener('click', function(event) {
            event.preventDefault(); // Предотвращаем переход по ссылке
            if (sitemapModal) {
                sitemapModal.style.display = 'block';
            }
        });
    }

    if (closeSitemapModal) {
        closeSitemapModal.addEventListener('click', function() {
            if (sitemapModal) {
                sitemapModal.style.display = 'none';
            }
        });
    }

    // Закрытие модального окна при клике вне его содержимого
    window.addEventListener('click', function(event) {
        if (sitemapModal && event.target == sitemapModal) {
            sitemapModal.style.display = 'none';
        }
    });
});

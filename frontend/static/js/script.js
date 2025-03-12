async function regFunction(event) {
    event.preventDefault();  // Предотвращаем стандартное действие формы

    // Получаем форму и собираем данные из неё
    const form = document.getElementById('registration-form');
    const formData = new FormData(form);
    const data = Object.fromEntries(formData.entries());
    try {
        const response = await fetch('/api/auth/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        // Проверяем успешность ответа
        if (!response.ok) {
            // Получаем данные об ошибке
            const errorData = await response.json();
            displayErrors(errorData);  // Отображаем ошибки
            return;  // Прерываем выполнение функции
        }

        const result = await response.json();

        if (result.message) {  // Проверяем наличие сообщения об успешной регистрации
            window.location.href = '/login';  // Перенаправляем пользователя на страницу логина
        } else {
            alert(result.message || 'Неизвестная ошибка');
        }
    } catch (error) {
        console.error('Ошибка:', error);
        alert('Произошла ошибка при регистрации. Пожалуйста, попробуйте снова.');
    }
}

async function loginFunction(event) {
    event.preventDefault();  // Предотвращаем стандартное действие формы

    // Получаем форму и собираем данные из неё
    const form = document.getElementById('login-form');
    const formData = new FormData(form);
    const data = Object.fromEntries(formData.entries());

    try {
        const response = await fetch('/api/auth/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        // Проверяем успешность ответа
        if (!response.ok) {
            // Получаем данные об ошибке
            const errorData = await response.json();
            displayErrors(errorData);  // Отображаем ошибки
            return;  // Прерываем выполнение функции
        }

        const result = await response.json();

        if (result.message) {  // Проверяем наличие сообщения об успешной регистрации
            window.location.href = '/profile';  // Перенаправляем пользователя на страницу логина
        } else {
            alert(result.message || 'Неизвестная ошибка');
        }
    } catch (error) {
        console.error('Ошибка:', error);
        alert('Произошла ошибка при входе. Пожалуйста, попробуйте снова.');
    }
}


async function gocreateStudent(event){
    window.location.href = '/create_student';
}

async function createStudent(event){
    event.preventDefault();  // Предотвращаем стандартное действие формы

    // Получаем форму и собираем данные из неё
    const form = document.getElementById('data-student');
    const formData = new FormData(form);
    const data = Object.fromEntries(formData.entries());
    try {
        const response = await fetch('/api/students/add/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        // Проверяем успешность ответа
        if (!response.ok) {
            // Получаем данные об ошибке
            const errorData = await response.json();
            displayErrors(errorData);  // Отображаем ошибки
            return;  // Прерываем выполнение функции
        }

        const result = await response.json();

        if (result.message) {  // Проверяем наличие сообщения об успешной регистрации
            window.location.href = '/profile';  // Перенаправляем пользователя на страницу профиля
        } else {
            alert(result.message || 'Неизвестная ошибка');
        }
    } catch (error) {
        console.error('Ошибка:', error);
        alert('Произошла ошибка при регистрации. Пожалуйста, попробуйте снова.');
    }
}


async function gocreateEmployer(event){
    window.location.href = '/create_employer';
}


async function createEmployer(event){
    event.preventDefault();  // Предотвращаем стандартное действие формы

    // Получаем форму и собираем данные из неё
    const form = document.getElementById('data-employer');
    const formData = new FormData(form);
    const data = Object.fromEntries(formData.entries());
    try {
        const response = await fetch('/api/employers/add/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        // Проверяем успешность ответа
        if (!response.ok) {
            // Получаем данные об ошибке
            const errorData = await response.json();
            displayErrors(errorData);  // Отображаем ошибки
            return;  // Прерываем выполнение функции
        }

        const result = await response.json();

        if (result.message) {  // Проверяем наличие сообщения об успешной регистрации
            window.location.href = '/profile';  // Перенаправляем пользователя на страницу профиля
        } else {
            alert(result.message || 'Неизвестная ошибка');
        }
    } catch (error) {
        console.error('Ошибка:', error);
        alert('Произошла ошибка при регистрации. Пожалуйста, попробуйте снова.');
    }
}

async function gocreateVacancy(event){
    window.location.href = '/create_vacancy';
}


async function createVacancy(event){
    event.preventDefault();  // Предотвращаем стандартное действие формы

    // Получаем форму и собираем данные из неё
    const form = document.getElementById('data-vacancy');
    const formData = new FormData(form);
    const data = Object.fromEntries(formData.entries());
    try {
        const response = await fetch('/api/vacancies/add/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        // Проверяем успешность ответа
        if (!response.ok) {
            // Получаем данные об ошибке
            const errorData = await response.json();
            displayErrors(errorData);  // Отображаем ошибки
            return;  // Прерываем выполнение функции
        }

        const result = await response.json();

        if (result.message) {  // Проверяем наличие сообщения об успешной регистрации
            window.location.href = '/vacancies';  // Перенаправляем пользователя на страницу профиля
        } else {
            alert(result.message || 'Неизвестная ошибка');
        }
    } catch (error) {
        console.error('Ошибка:', error);
        alert('Произошла ошибка при создании вакансии. Пожалуйста, попробуйте снова.');
    }
}


async function postApplication(event, id){
    event.preventDefault();
    try {
        let response = await fetch('/api/auth/me', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        });
        const result = await response.json();
        let student_id = result.student_id
        if (student_id) {
            let url = 'api/applications/?id_student='+ student_id + '&id_vacancy=' + id
            try {
                let response2 = await fetch(url,
                    {
                    method: 'GET',
                    headers: {
                        'Content-Type': 'application/json'}
        });
                let result1 = await response2.json();
                if (result1.length < 1) {
                    try {
                        let response3 = await fetch('/api/applications/add/', {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json'
                            },
                            body: JSON.stringify({
                                "id_student": student_id,
                                'id_vacancy': id
                            })
                        });
                        if (!response3.ok) {
                            // Получаем данные об ошибке
                            const errorData = await response3.json();
                            displayErrors(errorData);  // Отображаем ошибки
                            return;  // Прерываем выполнение функции
                        }
                        const result = await response3.json();
                        if (!result.message) {  // Проверяем наличие сообщения об успешной регистрации
                            alert(result.message || 'Неизвестная ошибка');  // Перенаправляем пользователя на страницу профиля
                        }
                    }
                    catch (error) {
                        console.error('Ошибка сети', error);
                    }
                }
                else {
                    alert('Уже есть заявка на эту вакансию')
                }
            } catch (error) {
                alert('Уже есть заявка на эту вакансию')
            }
        }
    else {
        alert('Нужно зарегистрироваться как студент')
        }
    } catch (error) {
        console.error('Ошибка сети', error);
    }
}

async function logoutFunction(event) {
    try {
        // Отправка POST-запроса для удаления куки на сервере
        let response = await fetch('/api/auth/logout', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        });

        // Проверка ответа сервера
        if (response.ok) {
            // Перенаправляем пользователя на страницу логина
            window.location.href = '/login';
        } else {
            // Чтение возможного сообщения об ошибке от сервера
            const errorData = await response.json();
            console.error('Ошибка при выходе:', errorData.message || response.statusText);
        }
    } catch (error) {
        console.error('Ошибка сети', error);
    }
}



async function profileFunction(event) {
    event.preventDefault();
    try {
        let response = await fetch('/api/auth/me', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        });
        const result = await response.json()
        // Проверка ответа сервера
        if (!result.detail) {
            window.location.href = '/profile';
        } else {
            window.location.href = '/login';
        }
    } catch (error) {
        console.error('Ошибка сети', error);
    }
}

async function checkAuthFunction(event) {
    try {
        let response = await fetch('/api/auth/me', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        });
        const result = await response.json();
        // Проверка ответа сервера
        if (result.detail) {
            window.location.href = '/login';
        }
    } catch (error) {
        console.error('Ошибка сети', error);
    }
}

async function bookingFunction(event) {
    event.preventDefault();
    const form = document.getElementById('booking-form');
    const formData = new FormData(form);
    let data = Object.fromEntries(formData.entries());
    console.log(data)
    try {
        let response = await fetch('/api/reservations/check/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
        let result = await response.json();
        // Проверка ответа сервера
        if (!result.ok) {
            displayErrors(result);
        } else {
            result = result.data
            let response2 = await fetch('/api/auth/me', {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json'
                }
            });
            response2 = await response2.json();
            user_id = response2.id

            let response3 = await fetch('/api/reservations/add/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({'name': result.name,
                    'date_from': result.date_from,
                    'date_to': result.date_to,
                    'object_id': result.object_id,
                    'user_id': user_id})
            });
            final = await response3.json();
            alert(final.message);
        }
    } catch (error) {
        console.error('Ошибка сети', error);
    }
}

async function deleteFunction(event) {
    let reservation = document.getElementById('res_id').textContent
    let current_url = '/api/reservations/dell/?reservation_id=' + reservation
    try {
        let response = await fetch(current_url, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            }
        });
        const result = await response.json();
        window.location.reload()
        alert(result.message)
    } catch (error) {
        console.error('Ошибка сети', error);
    }
}

// Функция для отображения ошибок
function displayErrors(errorData) {
    let message = 'Произошла ошибка';

    if (errorData && errorData.detail) {
        if (Array.isArray(errorData.detail)) {
            // Обработка массива ошибок
            message = errorData.detail.map(error => {
                if (error.type === 'string_too_short') {
                    return `Поле "${error.loc[1]}" должно содержать минимум ${error.ctx.min_length} символов.`;
                }
                if (error.type === 'string_too_long'){
                    return `Поле "${error.loc[1]}" должно содержать максимум ${error.ctx.max_length} символов.`;
                }
                return error.msg || 'Произошла ошибка';
            }).join('\n');
        } else {
            // Обработка одиночной ошибки
            message = errorData.detail || 'Произошла ошибка';
        }
    }
    // Отображение сообщения об ошибке
    alert(message);
}
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
                         // Проверяем наличие сообщения об успешной регистрации
                        alert(result.message || 'Неизвестная ошибка');  // Перенаправляем пользователя на страницу профиля
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
        console.error('Ошибка сервера', error);
    }
}

async function activateVac(event, id) {
    try {
        let url = 'api/vacancies/updateActive/' + id
        let response = fetch(url, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                is_active: true
            })
        })
        alert('Вакансия активирована')
        location.reload()
    } catch (error){
        alert('Ошибка сети')
    }
}


async function deactivateVac(event, id) {
    try {
        let url = 'api/vacancies/updateActive/' + id
        let response = fetch(url, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                is_active: false
            })
        })
        alert('Вакансия деактивирована')
        location.reload()
    } catch (error){
        alert('Ошибка сети')
    }
}


async function updStatus(event, student, vacancy, application, current_status, current_date, current_time, interview_id) {
    let new_status = document.getElementById("new_status");
    new_status = new_status.value;
    let interview = false
    let date = document.getElementById("date");
    date = date.value;
    let time = document.getElementById("time");
    time = time.value;
    if ((new_status === '3')){
        if (current_status !== "3"){
            let url2 = '/api/interviews/add/'
            try {
                const response2 = await fetch(url2, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        "id_student": student,
                        "id_vacancy": vacancy,
                        "date_start": date,
                        'time_start': time
                    })
                });
                if (!response2.ok) {
                    // Получаем данные об ошибке
                    const errorData = await response2.json();
                    displayErrors(errorData);  // Отображаем ошибки
                    return;  // Прерываем выполнение функции
                }
                else {
                    interview = true
                }
            } catch (error){
                const errorData = await response2.json();
                    displayErrors(errorData);  // Отображаем ошибки
                    return;
            }
        }
        else{
            if ((date !== current_date) || ((time + ':00')!== current_time)) {
                let url2 = '/api/interviews/update/' + interview_id
                try {
                    const response2 = await fetch(url2, {
                        method: 'PUT',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({
                            "date_start": date,
                            'time_start': time
                        })
                    });
                    if (!response2.ok) {
                        // Получаем данные об ошибке
                        const errorData = await response2.json();
                        displayErrors(errorData);  // Отображаем ошибки
                        return;  // Прерываем выполнение функции
                    }
                    else {
                        interview = true
                    }
                } catch (error){
                    const errorData = await response2.json();
                        displayErrors(errorData);  // Отображаем ошибки
                        return;
                }
            }
        }
    }
    if ((new_status === current_status) && (!interview)) {
        alert('Выбранный статус уже установлен');
    }
    else {
        if ((current_status === "3") && (new_status !== '3')) {
            let url3 = '/api/interviews/delete/' + interview_id
            try {
                    const response3 = await fetch(url3, {
                        method: 'DELETE',
                        headers: {
                            'Content-Type': 'application/json'
                        }
                    });
                    if (!response3.ok) {
                        // Получаем данные об ошибке
                        const errorData = await response3.json();
                        displayErrors(errorData);  // Отображаем ошибки
                        return;  // Прерываем выполнение функции
                    }
                } catch (error){
                    const errorData = await response3.json();
                        displayErrors(errorData);  // Отображаем ошибки
                        return;
                }
        }
        let url = '/api/applications/update/' + application;
        try {
            const response = await fetch(url, {
                method: 'PUT',
                headers: {
                'Content-Type': 'application/json'
            },
                body: JSON.stringify({
                                "id_status": new_status
                            })
            });
            if (response.ok){
                if (new_status === '3') {
                    alert('Статус обновлен, установлены дата и время собеседования')
                }
                else {
                    alert('Статус обновлен')
                }
                location.reload()
            }
        } catch (error) {
            displayErrors(error);
        }
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


async function deleteApplication(event, id) {
    let current_url = '/api/applications/delete/?application_id='+ id
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
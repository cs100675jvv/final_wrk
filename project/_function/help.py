def print_help():
    commands = [
        ("help", "Вивід допомоги по командам бота."),
        ("add [name] [phone]", "Додати новий контакт з іменем та номером телефону або номер телефону"),
        ("", "до існуючого контакту. Можна додати кілька номерів."),
        ("change [name] [old phone] [new phone]", "Змінити номер телефону для вказаного контакту."),
        ("phone [name]", "Показати номери телефонів для вказаного контакту."),
        ("all", "Показати всі контакти в адресній книзі."),
        ("add-birthday [name] [date of birth]", "Додати дату народження для вказаного контакту."),
        ("show-birthday [name]", "Показати дату народження для вказаного контакту."),
        ("change-birthday [name]", ""),
        ("birthdays", "Показати дні народження, які наближаються протягом наступного тижня."),
        ("add-email [name] [email]", "Додати email до контакту. Може бути кілька емейлів."),
        ("change-email [name] [old-email] [new-email]", "Змінити email для вказаного контакту."),
        ("add-address [name] [address]", "Додати адресу до контакту."),
        ("change-address [name] [address]", "Змінити адресу для вказаного контакту."),
        ("hello", "Надіслати привітання від бота."),
        ("add-note [name]", "Відкрити редактор для тексту нотатки. Введіть :end для завершення редагування."),
        ("", "Після цього нотатка буде додана."),
        ("list-notes", "Показати список всіх нотаток."),
        ("close або exit", "Закрити програму.")
    ]

    max_command_length = max(len(command) for command, _ in commands)
    
    print(f"{'Команда'.ljust(max_command_length)} | Опис")
    print("-" * (max_command_length + 3) + "+" + "-" * 70)

    for command, description in commands:
        print(f"{command.ljust(max_command_length)} | {description}")


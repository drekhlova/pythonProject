% sum_list([1,2,3,4,5,6,7,8,9,10], Sum).

% Источник: stackoverflow.com
% Определение предиката для вычисления суммы элементов списка
sum_list([], 0). % Базовый случай: сумма пустого списка равна 0
sum_list([Head|Tail], Sum) :- % Рекурсивный случай: сумма списка [Head|Tail] равна Head + сумме Tail
    sum_list(Tail, TailSum), % Вызываем рекурсивно sum_list для хвоста списка
    Sum is Head + TailSum. % Сумма списка [Head|Tail] равна Head + сумме Tail
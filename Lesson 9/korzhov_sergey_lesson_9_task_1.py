import time


class TrafficLight:
    __next_color = 'Красный'
    __last_colorRG = ''

    def __init__(self, color):
        self.__color = color

    def running(self):
        timings = {'Красный': 7, 'Желтый': 2, 'Зеленый': 10}
        current_light = self.__color
        try:
            if current_light != TrafficLight.__next_color:
                raise Exception(f'Нарушен порядок. Текущий сигнал {current_light}'
                                f' должен быть {TrafficLight.__next_color}')
            else:
                if current_light == 'Желтый':
                    if TrafficLight.__last_colorRG == 'Красный':
                        TrafficLight.__next_color = 'Зеленый'
                    else:
                        TrafficLight.__next_color = 'Красный'
                else:
                    TrafficLight.__next_color = 'Желтый'
                    TrafficLight.__last_colorRG = current_light

                timing = timings[current_light]
                print(f'Горит {current_light}. Продолжительность {timing} сек.')
                time.sleep(timing)

        except KeyError as k:
            print('KeyError', k)


t = TrafficLight('Красный')
t.running()
t = TrafficLight('Желтый')
t.running()
t = TrafficLight('Зеленый')
t.running()
t = TrafficLight('Желтый')
t.running()
t = TrafficLight('Красный')
t.running()
t = TrafficLight('Зеленый')
t.running()

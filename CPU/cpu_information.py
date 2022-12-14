import psutil


def get_cpu_information():
    print('=' * 40, 'CPU information', '=' * 40)

    print('Physical cores: ', psutil.cpu_count(logical=False))
    print('Total cores: ', psutil.cpu_count(logical=True))

    cpufreq = psutil.cpu_freq()
    print(f'Maximum frequency: {round(cpufreq.max, 2)}MHz')
    print(f'Minimal frequency: {round(cpufreq.min, 2)}MHz')
    print(f'Current frequency: {round(cpufreq.current, 2)}MHz')

    print('CPU usage on core:')
    for i, perc in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        print(f'Core {i}: {perc}%')
    print(f'Total CPU usage: {psutil.cpu_percent()}%')

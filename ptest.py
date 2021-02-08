import multiprocessing
import logging
import time


root_logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter(
    '%(asctime)s %(name)-15s %(levelname)-4s %(message)s', '%Y-%m-%d %H:%M:%S')
handler.setFormatter(formatter)
root_logger.addHandler(handler)
root_logger.setLevel(logging.DEBUG)

logger = logging.getLogger(__name__)

def f(sleep_seconds):
    logger.info("Sleeping for %d seconds", sleep_seconds)
    print('I am going to sleep')
    time.sleep(sleep_seconds)
    print('I am awake')
    logger.info('Done sleeping')
    with open('done.txt', 'w') as d:
      d.write('done!')


if __name__ == '__main__':
    logger.info('Starting background process')
    p = multiprocessing.Process(target=f, args=(5,))
    p.start()
    p.join()

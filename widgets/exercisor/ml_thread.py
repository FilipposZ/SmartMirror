from abc import ABC, abstractclassmethod
import threading
import time
from log import logger


class MLThread(ABC, threading.Thread):
    """
    The abstract implementation of a machine learning module that will be run on a separate thread.
    The thread executes instantly when it is constructed so that the model will start loading
    and then it enters the paused state.

    Attributes
    ----------
    model_name: str
        The name of the AI model that will be executed.
    name: str
        The name of the thread.
    target_fps:
        The maximum number of predictions per second.

    Methods
    -------
    pause()
        Pauses the execution of the thread.
    resume()
        Resumes the execution of the thread.
    stop()
        Stops the execution of the thread.
    is_paused()
        Returns True if the thread is paused, False otherwise.
    run()
        The execution method of the thread.
    prepare_model()
        Prepare and load the AI model.
    prepare_inputs()
        Prepare the inputs that will be used in the current prediction.
    predict(inputs)
        Use the inputs to predict the outputs.
    process_outputs(outputs)
        Process the outputs and/or use them.
    cleaning_up()
        Release the acquired resources when the prediction loop finishes.
    """

    def __init__(self, model_name=None, target_fps=25, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.model_name = model_name
        self.name = self.model_name + 'Thread'
        self.target_fps = target_fps
        self.output_fn = None

        self._resumed = threading.Event()
        self._running = threading.Event()
        self._running.set()
        self.start()

    def pause(self):
        self._resumed.clear()

    def resume(self):
        self._resumed.set()

    def stop_exec(self):
        self._running.clear()

    def is_paused(self):
        return not self._resumed.is_set()

    def run(self, *args, **kwargs):

        logger.info(f'Loading {self.model_name}...')
        self.prepare_model()
        logger.info(f'Loaded the {self.model_name} model')

        while(self._running.is_set()):
            self._resumed.wait()
            self.start_time = time.time()
            inputs = self.prepare_inputs()
            outputs = self.predict(inputs)
            self.process_outputs(outputs)

            # If processing finished fast, sleep to guarantee the target_fps
            time.sleep(max(1./self.target_fps - (time.time() - self.start_time), 0))

        self.cleaning_up()
        logger.info(f'{self.name} has finished execution')

    @abstractclassmethod
    def prepare_model(self):
        pass

    @abstractclassmethod
    def prepare_inputs(self):
        pass

    @abstractclassmethod
    def predict(self):
        pass

    @abstractclassmethod
    def process_outputs(self):
        pass

    @abstractclassmethod
    def cleaning_up(self):
        pass

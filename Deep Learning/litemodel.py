# -*- coding: utf-8 -*-
"""
Created on Fri May  8 12:59:01 2020

@author: Zikantika
"""

import numpy as np
import tensorflow as tf
from pathlib import Path

# Load the MobileNet keras model.
# we will create tf.keras model by loading pretrained model on #imagenet dataset
model = tf.keras.applications.MobileNetV2(
    weights="imagenet", input_shape=(224, 224, 3))
# here we pretrained model no need use SaveModel 
# here we will pass model directly to TFLiteConverter
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()


#converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
#converter.optimizations = [tf.lite.Optimize.DEFAULT]
#tflite_quant_model = converter.convert()

#converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
#converter.optimizations = [tf.lite.Optimize.DEFAULT]
#converter.target_spec.supported_types = [tf.lite.constants.FLOAT16]
#tflite_quant_model = converter.convert()

#converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]
#converter.inference_input_type = tf.uint8
#converter.inference_output_type = tf.uint8



###if you want to save the TF Lite model use below steps or else skip
#tflite_model_files = pathlib.Path('/tmp/pretrainedmodel.tflite')
#tflite_model_file.write_bytes(tflite_model)

tflite_model_files = Path('pretrainedmodel.tflite')
tflite_model_files.write_bytes(tflite_model)

# Load TFLite model using interpreter and allocate tensors.
interpreter = tf.lite.Interpreter(model_content=tflite_model)
interpreter.allocate_tensors()
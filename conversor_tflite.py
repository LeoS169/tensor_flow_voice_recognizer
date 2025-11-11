import tensorflow as tf
diretorio_savedModel = r"models\primeiro_modelo"

# Criação do conversor
conversor = tf.lite.TFLiteConverter.from_saved_model(diretorio_savedModel)

# Conversão do modelo
modelo_tflite = conversor.convert()

# Escrita do modelo em um arquivo .tflite
with open("models_tflite/model.tflite", "wb") as f:
    f.write(modelo_tflite)
    
    
    
    
    
    
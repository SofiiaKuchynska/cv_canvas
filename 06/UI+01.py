import numpy as np
import matplotlib.pyplot as plt
import gradio as gr

def train_linear_model():
    x = np.linspace(0, 10, 20)
    y = np.linspace(-10, 100, 20)
    n = len(x)
    m = (n * np.sum(x * y) - np.sum(x) * np.sum(y)) / (n * np.sum(x ** 2) - np.sum(x) ** 2)
    b = (np.sum(y) - m * np.sum(x)) / n
    return m, b, x, y

M_COEFF, B_COEFF, X_DATA, Y_DATA = train_linear_model()

def predict_and_plot(x_input):
    y_output = M_COEFF * x_input + B_COEFF
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.scatter(X_DATA, Y_DATA, color='red', label='Дані для навчання')
    y_pred_line = M_COEFF * X_DATA + B_COEFF
    ax.plot(X_DATA, y_pred_line, color='blue', label=f'Лінія: y={M_COEFF:.2f}x + {B_COEFF:.2f}')
    ax.scatter(x_input, y_output, color='green', s=150, zorder=5, label=f'Твій вибір (X={x_input:.1f})')
    ax.legend()
    ax.set_title("Прогноз за методом найменших квадратів")
    ax.grid(True)
    return f"Для X = {x_input:.2f} отримано результат Y = {y_output:.2f}", fig
interface = gr.Interface(
    fn=predict_and_plot,
    inputs=gr.Slider(minimum=0, maximum=100, value=5, step=2, label="Виберіть значення X"),
    outputs=[
        gr.Textbox(label="Результат Y"),
        gr.Plot(label="Візуалізація моделі")
    ],
    title="Інтерактивний МНК-калькулятор",
    description="Пересувай повзунок X, щоб побачити прогноз Y та де саме ця точка знаходиться на графіку лінії регресії.",
    submit_btn="Розрахувати"
)
if __name__ == "__main__":
    interface.launch()
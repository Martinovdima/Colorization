Colorization is a Telegram bot — @image_filter_late_bot
 — that processes user images by applying filters and performing automatic colorization of black-and-white photos using the pre-trained DeOldify neural network.
 <img width="736" height="736" alt="start" src="https://github.com/user-attachments/assets/a8b59d2a-0b71-44a9-a355-f20a1ab09823" />

1. This is an educational project demonstrating how OpenCV can be used for image processing and integrated into a Telegram bot with AI features.

The bot includes 12 different filters demonstrating the power of OpenCV:

Pixel

Sepia

Cartoon

Pencil

Black-and-white conversion

HDR

Blur

And more

📷 Example:
Before ➜ After applying a filter
<img width="1000" height="1000" alt="help" src="https://github.com/user-attachments/assets/099a3991-be97-42ca-a959-ccadce8c3a5e" />

2. The bot uses the DeOldify model to colorize black-and-white or old photographs.
The model has been trained on a large dataset and can restore realistic colors with high accuracy.

📷 Example:
Before -> After colorization:
<img width="740" height="1295" alt="black-white-palm-landscape_23-2151601904" src="https://github.com/user-attachments/assets/2f7d6480-072b-4745-80e9-193787a7e377" />
<img width="731" height="1280" alt="color-palm-landscape_23-2151601904" src="https://github.com/user-attachments/assets/24efa941-06e3-43b8-9b21-6becc1c0b205" />

🧠 Technologies

Python 3.10+

OpenCV — image processing

DeOldify — neural network for colorization

Telegram Bot API — user interaction

NumPy, Pillow, Torch — supporting libraries

⚙️ Installation and Usage
1. Clone the repository
git clone https://github.com/Martinovdima/Colorization.git
cd Colorization

2. Install dependencies
pip install -r requirements.txt

3. Install DeOldify

The DeOldify library is installed separately.
Follow the instructions in manual.txt
.

4. Run the bot
python main.py


🧾 Licenses

The project source code is distributed under the MIT License

OpenCV is used under the Apache 2.0 License.

DeOldify is used under the MIT License.

👤 Author

Timo Martin
Telegram: @image_filter_late_bot



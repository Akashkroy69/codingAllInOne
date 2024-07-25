import random
import pyautogui as pg
import time
# from faker import Faker
# fake = Faker()

# test = ["motto koot denge","pahchanti hai tum hmko?"]

# listOfWords = []
# for i in range(500):
#     message = "SORRY, number: " + str(i)
#     listOfWords.append(message)
# # print(random.choice(listOfWords))

tweets = [
    "1. Embrace challenges with a smile; they shape you into a stronger person. 8Yrs Of KKK7 Winner Sidharth 🎉",
    "2. Surround yourself with positivity and watch your world transform. 8Yrs Of KKK7 Winner Sidharth 🌟",
    "3. Cherish the present moment, for it's a gift that shapes your future. 8Yrs Of KKK7 Winner Sidharth 🎁",
    "4. Strive for progress, not perfection. Every step forward is a victory. 8Yrs Of KKK7 Winner Sidharth 🚀",
    "5. Take risks, step out of your comfort zone, and discover the magic of growth. 8Yrs Of KKK7 Winner Sidharth ✨",
    "6. Practice gratitude daily; it's the key to a happy and fulfilled life. 8Yrs Of KKK7 Winner Sidharth 🙏",
    "7. Be kind to yourself; you are a work in progress, constantly evolving. 8Yrs Of KKK7 Winner Sidharth 💖",
    "8. Learn from failures; they are stepping stones to success. 8Yrs Of KKK7 Winner Sidharth 🌈",
    "9. Cultivate meaningful connections; relationships are the true wealth of life. 8Yrs Of KKK7 Winner Sidharth 👫",
    "10. Your attitude determines your direction. Stay positive, stay focused. 8Yrs Of KKK7 Winner Sidharth 🌠",
    "11. Embrace change; it's the only constant in life. 8Yrs Of KKK7 Winner Sidharth 🔄",
    "12. Set goals that inspire you and work towards them with passion. 8Yrs Of KKK7 Winner Sidharth 🎯",
    "13. Take time for self-reflection; it's a journey to self-discovery. 8Yrs Of KKK7 Winner Sidharth 🔍",
    "14. Success is a journey, not a destination. Enjoy the ride. 8Yrs Of KKK7 Winner Sidharth 🚗",
    "15. Find joy in the little things; they often hold the most significance. 8Yrs Of KKK7 Winner Sidharth 🌺",
    "16. Practice mindfulness; it brings you closer to the beauty of the present. 8Yrs Of KKK7 Winner Sidharth 🧘",
    "17. Surround yourself with those who lift you higher. 8Yrs Of KKK7 Winner Sidharth 🚀",
    "18. Don't be afraid to ask for help; strength lies in vulnerability. 8Yrs Of KKK7 Winner Sidharth 🤝",
    "19. Your story is unique; embrace it with all its twists and turns. 8Yrs Of KKK7 Winner Sidharth 📖",
    "20. Success is not a sprint but a marathon. Keep going. 8Yrs Of KKK7 Winner Sidharth 🏃‍♂️",
    "21. Take care of your mental health; it's as important as your physical well-being. 8Yrs Of KKK7 Winner Sidharth 🧠",
    "22. Celebrate your achievements, no matter how small. 8Yrs Of KKK7 Winner Sidharth 🎉",
    "23. Let go of what you can't control; focus on what you can change. 8Yrs Of KKK7 Winner Sidharth 🔄",
    "24. Keep learning; the world is a vast classroom. 8Yrs Of KKK7 Winner Sidharth 📚",
    "25. Be authentic; there's power in being true to yourself. 8Yrs Of KKK7 Winner Sidharth 💪",
    "26. Time is your most valuable asset; use it wisely. 8Yrs Of KKK7 Winner Sidharth ⌛",
    "27. Face challenges with courage; they are opportunities in disguise. 8Yrs Of KKK7 Winner Sidharth 🛡️",
    "28. Stay curious; curiosity fuels creativity and innovation. 8Yrs Of KKK7 Winner Sidharth 🤔",
    "29. Practice patience; good things take time to blossom. 8Yrs Of KKK7 Winner Sidharth 🌸",
    "30. Connect with nature; it has a way of grounding and rejuvenating your spirit. 8Yrs Of KKK7 Winner Sidharth 🌳",
    "31. Express gratitude not just for what you have but for who you are becoming. 8Yrs Of KKK7 Winner Sidharth 🙌",
    "32. Be a lifelong learner; the quest for knowledge is a journey without end. 8Yrs Of KKK7 Winner Sidharth 🌐",
    "33. Cultivate resilience; it's the armor that protects you in the face of adversity. 8Yrs Of KKK7 Winner Sidharth 🛡️",
    "34. Strive for balance in all aspects of life; it's the key to lasting happiness. 8Yrs Of KKK7 Winner Sidharth ⚖️",
    "35. Follow your heart; it knows the way. 8Yrs Of KKK7 Winner Sidharth ❤️",
     "1. 8Yrs Of KKK7 Winner Sidharth! 🎉 Set clear goals for your studies; they give you direction and purpose. 🎯",
    "2. 8Yrs Of KKK7 Winner Sidharth! 🌟 Find a study routine that works for you and stick to it consistently. ⏰",
    "3. 8Yrs Of KKK7 Winner Sidharth! 🎁 Break down complex topics into smaller, manageable tasks for effective learning. 📚",
    "4. 8Yrs Of KKK7 Winner Sidharth! 🚀 Stay organized; use planners and calendars to keep track of assignments and deadlines. 🗓️",
    "5. 8Yrs Of KKK7 Winner Sidharth! ✨ Embrace active learning techniques like summarizing, teaching, and problem-solving. 📝",
    "6. 8Yrs Of KKK7 Winner Sidharth! 🙏 Take regular breaks during study sessions to maintain focus and prevent burnout. ⏸️",
    "7. 8Yrs Of KKK7 Winner Sidharth! 💖 Build a productive study environment; eliminate distractions and create a comfortable space. 🌟",
    "8. 8Yrs Of KKK7 Winner Sidharth! 🌈 Connect with fellow students; group study sessions can enhance your understanding of topics. 👥",
    "9. 8Yrs Of KKK7 Winner Sidharth! 👫 Seek help when needed; don't hesitate to ask teachers, peers, or online resources. 🆘",
    "10. 8Yrs Of KKK7 Winner Sidharth! 🌠 Stay curious and approach learning with a mindset of exploration and discovery. 🔍",
    "11. 8Yrs Of KKK7 Winner Sidharth! 🎯 Use a variety of study resources, including textbooks, online materials, and multimedia. 📖",
    "12. 8Yrs Of KKK7 Winner Sidharth! 🔍 Take effective notes during lectures; it enhances memory retention and understanding. 🗒️",
    "13. 8Yrs Of KKK7 Winner Sidharth! 🚗 Create a study schedule that includes review sessions to reinforce what you've learned. 🔄",
    "14. 8Yrs Of KKK7 Winner Sidharth! 🎓 Set realistic expectations; understand that learning is a process, not a race. 🏃‍♂️",
    "15. 8Yrs Of KKK7 Winner Sidharth! 🌺 Prioritize self-care; a healthy mind and body contribute to effective learning. 💪",
    "16. 8Yrs Of KKK7 Winner Sidharth! 🧘 Practice mindfulness to stay present and focused during study sessions. 🧠",
    "17. 8Yrs Of KKK7 Winner Sidharth! 🚀 Utilize technology for learning; there are many apps and online tools to enhance your studies. 📱",
    "18. 8Yrs Of KKK7 Winner Sidharth! 🤝 Form study groups for collaborative learning and sharing different perspectives. 👥",
    "19. 8Yrs Of KKK7 Winner Sidharth! 📚 Explore different study methods to find what suits your learning style best. 📖",
    "20. 8Yrs Of KKK7 Winner Sidharth! 🎉 Celebrate small victories during your study journey; progress is worth acknowledging. 🎊",
    "21. 8Yrs Of KKK7 Winner Sidharth! 🌍 Stay informed about global trends and advancements related to your field of study. 🌐",
    "22. 8Yrs Of KKK7 Winner Sidharth! 🛡️ Develop resilience; setbacks are part of the learning process. Bounce back stronger. 💪",
    "23. 8Yrs Of KKK7 Winner Sidharth! ⚖️ Maintain a balance between academic and personal life for overall well-being. ⚖️",
    "24. 8Yrs Of KKK7 Winner Sidharth! 📚 Use mnemonic devices and visualization techniques to aid memory recall. 🧠",
    "25. 8Yrs Of KKK7 Winner Sidharth! ⌛ Practice time management; allocate dedicated time slots for each subject and task. ⏰",
    "26. 8Yrs Of KKK7 Winner Sidharth! 🛡️ Embrace challenges; they are opportunities for intellectual growth. 🚀",
    "27. 8Yrs Of KKK7 Winner Sidharth! 🤔 Develop critical thinking skills; question, analyze, and evaluate information. 🤔",
    "28. 8Yrs Of KKK7 Winner Sidharth! 🌺 Foster a love for lifelong learning; education extends beyond the classroom. 🌟",
    "29. 8Yrs Of KKK7 Winner Sidharth! 📖 Explore diverse perspectives and theories within your field of study. 🌐",
    "30. 8Yrs Of KKK7 Winner Sidharth! 🏃‍♂️ Stay adaptable; the ability to learn and unlearn is crucial in a dynamic world. 🔄",
    "31. 8Yrs Of KKK7 Winner Sidharth! 🙌 Collaborate with mentors and professionals in your field; networking is key. 👥",
    "32. 8Yrs Of KKK7 Winner Sidharth! 🌟 Reflect on your academic journey; celebrate growth and set new learning goals. 🎓",
    "33. 8Yrs Of KKK7 Winner Sidharth! 🛡️ Face challenges with a positive mindset; they are opportunities in disguise. 🚀",
    "34. 8Yrs Of KKK7 Winner Sidharth! ❤️ Stay passionate about your studies; genuine interest fuels motivation. 🔥",
    "35. 8Yrs Of KKK7 Winner Sidharth! 🌟 Believe in your potential; you have the capacity to achieve greatness. 💪",
     "1. 8Yrs Of KKK7 Winner Sidharth! 🎉 \"Believe you can, and you're halfway there.\" - Theodore Roosevelt",
    "2. 8Yrs Of KKK7 Winner Sidharth! 🌟 \"The only way to do great work is to love what you do.\" - Steve Jobs",
    "3. 8Yrs Of KKK7 Winner Sidharth! 🎁 \"Your time is limited, don't waste it living someone else's life.\" - Steve Jobs",
    "4. 8Yrs Of KKK7 Winner Sidharth! 🚀 \"Success is not final, failure is not fatal: It is the courage to continue that counts.\" - Winston Churchill",
    "5. 8Yrs Of KKK7 Winner Sidharth! ✨ \"The only limit to our realization of tomorrow will be our doubts of today.\" - Franklin D. Roosevelt",
    "6. 8Yrs Of KKK7 Winner Sidharth! 🙏 \"The future belongs to those who believe in the beauty of their dreams.\" - Eleanor Roosevelt",
    "7. 8Yrs Of KKK7 Winner Sidharth! 💖 \"Success is stumbling from failure to failure with no loss of enthusiasm.\" - Winston S. Churchill",
    "8. 8Yrs Of KKK7 Winner Sidharth! 🌈 \"Your work is going to fill a large part of your life, and the only way to be truly satisfied is to do what you believe is great work.\" - Steve Jobs",
    "9. 8Yrs Of KKK7 Winner Sidharth! 👫 \"Strive not to be a success, but rather to be of value.\" - Albert Einstein",
    "10. 8Yrs Of KKK7 Winner Sidharth! 🌠 \"The only person you are destined to become is the person you decide to be.\" - Ralph Waldo Emerson",
    "11. 8Yrs Of KKK7 Winner Sidharth! 🎯 \"The only thing standing between you and your goal is the story you keep telling yourself as to why you can't achieve it.\" - Jordan Belfort",
    "12. 8Yrs Of KKK7 Winner Sidharth! 🔍 \"The way to get started is to quit talking and begin doing.\" - Walt Disney",
    "13. 8Yrs Of KKK7 Winner Sidharth! 🔄 \"I find that the harder I work, the more luck I seem to have.\" - Thomas Jefferson",
    "14. 8Yrs Of KKK7 Winner Sidharth! 🎓 \"Success is not in what you have, but who you are.\" - Bo Bennett",
    "15. 8Yrs Of KKK7 Winner Sidharth! 🌺 \"Your time is now. Start where you are, use what you have, and do what you can.\" - Arthur Ashe",
    "16. 8Yrs Of KKK7 Winner Sidharth! 🧘 \"The only way to achieve the impossible is to believe it is possible.\" - Charles Kingsleigh",
    "17. 8Yrs Of KKK7 Winner Sidharth! 🚀 \"It always seems impossible until it's done.\" - Nelson Mandela",
    "18. 8Yrs Of KKK7 Winner Sidharth! 🤝 \"Success is not just about making money. It's about making a difference.\" - Unknown",
    "19. 8Yrs Of KKK7 Winner Sidharth! 📚 \"Do not wait to strike till the iron is hot, but make it hot by striking.\" - William Butler Yeats",
    "20. 8Yrs Of KKK7 Winner Sidharth! 🎉 \"Success usually comes to those who are too busy to be looking for it.\" - Henry David Thoreau",
    "21. 8Yrs Of KKK7 Winner Sidharth! 🌍 \"Don't watch the clock; do what it does. Keep going.\" - Sam Levenson",
    "22. 8Yrs Of KKK7 Winner Sidharth! 🛡️ \"Don't be pushed around by the fears in your mind. Be led by the dreams in your heart.\" - Roy T. Bennett",
    "23. 8Yrs Of KKK7 Winner Sidharth! ⚖️ \"Success is stumbling from failure to failure with no loss of enthusiasm.\" - Winston S. Churchill",
    "24. 8Yrs Of KKK7 Winner Sidharth! 📚 \"Education is the most powerful weapon which you can use to change the world.\" - Nelson Mandela",
    "25. 8Yrs Of KKK7 Winner Sidharth! ⌛ \"The best way to predict the future is to create it.\" - Peter Drucker",
    "26. 8Yrs Of KKK7 Winner Sidharth! 🛡️ \"Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.\" - Christian D. Larson",
    "27. 8Yrs Of KKK7 Winner Sidharth! 🤔 \"The only place where success comes before work is in the dictionary.\" - Vidal Sassoon",
    "28. 8Yrs Of KKK7 Winner Sidharth! 🌺 \"You have within you right now, everything you need to deal with whatever the world can throw at you.\" - Brian Tracy",
    "29. 8Yrs Of KKK7 Winner Sidharth! 📖 \"Don't be afraid to give up the good to go for the great.\" - John D. Rockefeller",
    "30. 8Yrs Of KKK7 Winner Sidharth! 🏃‍♂️ \"What lies behind us and what lies before us are tiny matters compared to what lies within us.\" - Ralph Waldo Emerson",
    "31. 8Yrs Of KKK7 Winner Sidharth! 🙌 \"The road to success and the road to failure are almost exactly the same.\" - Colin R. Davis",
    "32. 8Yrs Of KKK7 Winner Sidharth! 🌟 \"If you want to achieve greatness, stop asking for permission.\" - Unknown",
    "33. 8Yrs Of KKK7 Winner Sidharth! 🛡️ \"Don't be afraid to stand for what you believe in, even if that means standing alone.\" - Unknown",
    "34. 8Yrs Of KKK7 Winner Sidharth! ❤️ \"Don't watch the clock; do what it does. Keep going.\" - Sam Levenson",
    "35. 8Yrs Of KKK7 Winner Sidharth! 🌟 \"The only way to do great work is to love what you do.\" - Steve Jobs"
]

android_dev_messages = [
    "1. Android development offers endless opportunities for innovation and creativity.",
    "2. Learn Android development to build powerful and user-friendly mobile apps.",
    "3. Mastering Android development opens doors to lucrative career opportunities.",
    "4. Dive into Android development to create apps that millions of users can enjoy.",
    "5. Android development skills are in high demand in today's tech industry.",
    "6. Explore the world of Android development and bring your app ideas to life.",
    "7. Android development allows you to build apps for smartphones, tablets, wearables, and more.",
    "8. Stay updated with the latest trends and technologies in Android development.",
    "9. Android development offers flexibility and customization for building unique apps.",
    "10. Join the vibrant Android developer community and collaborate with fellow developers.",
    "11. Kotlin has become the preferred language for Android development due to its concise syntax and powerful features.",
    "12. Dive deep into Android Studio, the official IDE for Android development, and unleash its full potential.",
    "13. Design beautiful and intuitive user interfaces for your Android apps.",
    "14. Implement responsive layouts that adapt to different screen sizes and orientations.",
    "15. Leverage Android's rich set of APIs to add advanced features to your apps.",
    "16. Optimize your Android apps for performance and efficiency to provide a smooth user experience.",
    "17. Test your Android apps thoroughly to ensure they are bug-free and reliable.",
    "18. Secure your Android apps against common vulnerabilities and protect user data.",
    "19. Publish your Android apps on the Google Play Store and reach a global audience.",
    "20. Stay informed about Google's guidelines and policies for Android app development.",
    "21. Embrace Material Design principles to create visually appealing and consistent user interfaces.",
    "22. Explore the Android Jetpack components to accelerate your app development process.",
    "23. Implement navigation patterns that enhance usability and navigation within your Android apps.",
    "24. Use RecyclerView to efficiently display large datasets and lists in your Android apps.",
    "25. Integrate third-party libraries and APIs to extend the functionality of your Android apps.",
    "26. Implement background tasks and services to perform long-running operations without blocking the main UI thread.",
    "27. Leverage Firebase services to add real-time data syncing, authentication, and analytics to your Android apps.",
    "28. Master the principles of responsive design to create adaptive and flexible layouts for different devices.",
    "29. Implement offline capabilities in your Android apps to provide a seamless user experience even without an internet connection.",
    "30. Utilize Android's notification system to keep users informed and engaged with your app.",
    "31. Leverage the power of Android's location services to build location-aware apps.",
    "32. Explore the world of augmented reality (AR) and virtual reality (VR) in Android app development.",
    "33. Implement in-app purchases and monetization strategies to generate revenue from your Android apps.",
    "34. Optimize your Android apps for battery efficiency to prolong device battery life.",
    "35. Stay up-to-date with the latest security best practices and guidelines for Android app development.",
    "36. Use Android's multimedia capabilities to create engaging and interactive experiences in your apps.",
    "37. Implement user authentication and authorization mechanisms to secure access to your app's features and content.",
    "38. Leverage machine learning and artificial intelligence to add intelligent features to your Android apps.",
    "39. Implement data caching and prefetching strategies to improve the performance of your Android apps.",
    "40. Utilize Android's camera and image processing capabilities to create photo and video editing apps.",
    "41. Master the art of debugging and troubleshooting to identify and fix issues in your Android apps.",
    "42. Optimize your app's memory usage to ensure efficient resource utilization and prevent crashes.",
    "43. Explore the world of game development on Android and create immersive gaming experiences.",
    "44. Implement push notifications to keep users engaged and informed about updates and new content.",
    "45. Utilize Android's background execution limits to optimize battery usage and improve overall system performance.",
    "46. Stay informed about the latest Android platform updates and features to stay ahead of the curve.",
    "47. Use analytics and user feedback to continuously improve and iterate on your Android apps.",
    "48. Implement accessibility features to ensure that your Android apps are usable by all users, including those with disabilities.",
    "49. Leverage cloud services and storage solutions to scale your Android apps and handle large amounts of data.",
    "50. Never stop learning and experimenting with new technologies and techniques in Android development."
]






time.sleep(20)
for i in range(len(android_dev_messages)):
    pg.click()
    pg.write(android_dev_messages[i])

    # pg.press("enter") 
    pg.hotkey('ctrl', 'enter')
    time.sleep(5)

    # pg.hotkey('enter')







  # pg.write(""+a)
    # pg.press("enter")
    # pg.write("======")
    # pg.press("enter")

# pg.hotkey("ctrl","s")

# pg.write(random.__name__)

# pg.press("enter")
title: AI in healthcare
description: Ai is playing an increasingly important role in healthcare.
groups: rtc
picture: projects/ai_for_health.png

{% extends "base.html" %}
{% block title %}{{ Course }}{%endblock%}
{% block description %}Course for ai-for-health{% endblock %}
{% block page_picture %}{{ SITEURL }}/{{SITE_PICTURE}}{% endblock %}
{% block content %}
{% include 'blocks/breadcrumbs.html' %}

<div class="container">
    <h1 class="page-title">{{ Courses }} </h1>
    <h1> AI for Health course </h1>
    Have you ever thought about exploring and understanding the field of artificial intelligence? Due to the successes in past years, the AI for Health course will also be held in Q1 2025. This course, designed specifically for clinicians, researchers and support staff working in hospitals, provides insight and hands-on experience into the many possibilities of artificial intelligence in healthcare. 
    <br/>
    If you are interested in joining the next course, you can express your interest by sending an email to <aiforhealth@radboudumc.nl> and we will keep you up to date when more information regarding a start date becomes available.
    <br/>
    <br/>
    To meet the needs of our participants as much as possible, we offer two different tracks:

    <ul>
        <li> <b>light track</b>, in which you get a good overview of the role AI can have in clinical practice.</li>
        <li> <b>full track</b>, in which you will, on top of the content you get in the light track, also learn to implement AI solutions yourself using Python.</li>
    </ul>

    Following our tracks you will:

    <ul>
        <li>Gain insight in how artificial intelligence can impact healthcare.</li>
        <li>Gain insight in the essential ingredients to run a successful AI project.</li>
        <li>Gain knowledge on how to choose the best AI models and AI products available.</li>
        <li>Gain knowledge on how AI models work and how performances can be optimized.</li>   
        <li>Learn how to implement your own AI models by exercising in practical settings (full track only!).</li>
    </ul>

    This course is a must for:
    
    <ul>
        <li>Anyone wanting to support decision making processes through the use of healthcare data.</li>
        <li>Anyone believing there is more potential in healthcare data than is currently being exploited.</li>
        <li>Anyone interested in understanding the possibilities and limitations of using artificial intelligence to improve healthcare.</li>
    </ul>
    
    More information can be found below.
    

    <!--Artificial intelligence (AI) is playing an increasingly important role in healthcare, offering healthcare professionals great opportunities to improve the care they provide. Radboud AI for Health, in collaboration with Jheronimus Academy of Data Science (<a href="https://www.jads.nl/">JADS</a>), offers the AI for Health course for clinicians, researchers and support staff working in hospitals. The next edition will start on <b>11-02-2022</b>. Apply before <b>17-12-2021</b> to join the course.
    <br/>
    <br/>
    <b>For whom is this course?</b>
    <ul>
      <li>Anyone believing there is more potential in healthcare data than is currently made use of.</li>
      <li>Anyone wanting to support decision making processes through the use of healthcare data.</li>
      <li>Anyone interested in getting an overview of the different possibilities and limitations of using AI to improve healthcare.  </li>
    </ul>
    Successful AI projects draw upon clinical expertise, data expertise as well as programming expertise. This makes the AI for Health course just as relevant to clinicians as to professionals with a strong background in programming, statistics and/or data analytics. To meet the needs of participants with different backgrounds as much as possible, the course offers <b>2 tracks</b>.
    <br/>
    <br/>
    <b>Which track should I follow?</b>
    <ul>
    <li>Participants can choose to follow the 17 day <b>full track</b>, where they will learn to implement AI themselves using Python.</li>
    <li>Alternatively, they can follow the 10 half-day <b>light track</b>, which provides a good overview of the role AI can have in clinical practice, without any programming involved.</li>
    </ul>
    Both tracks introduce the most important AI concepts such as machine learning and deep learning and all the necessary ingredients for a successful AI implementation, such as data understanding and preparation, and model evaluation. Different fields of AI applications are covered, such as medical image analysis, text mining and bioinformatics. The in-depth track provides participants also with practical exercises where they implement their own AI solutions. At the end of the course, participants will work in teams on their own AI project, where they get a feeling how to successfully create your own AI implementation.
    <br/>
    <br/>
    
    <b>What do I get out of the course?</b>
    <ul>
      <li>A great overview of how AI can impact healthcare.</li>
      <li>Insight in the necessary ingredients to run a successful AI project.</li>
      <li>A good understanding of how AI models work and how to optimize their performance.</li>
      <li>Tips and tricks on how to choose the best AI model or ready-to-use AI products.</li>
      <li>Full track only: Hands-on experience implementing your own AI models. The best way to learn about AI is by doing it!</li>
    </ul> 
    
    For more information about the course, see below.-->
    <div class="row mt-4">
        {% for card in pages %}
            {% if card.category == 'courses' %}
                {% include "blocks/card.html" %}
            {% endif %}
        {% endfor %}
    </div>
</div>
{% endblock %}

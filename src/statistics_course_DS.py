import streamlit as st

def statistics_ds_course():
    st.markdown("""

        <img src="https://audreytips.com/wp-content/uploads/2021/06/comment-utiliser-le-rapport-d-experience-de-la-page-de-la-console-de-recherche-google.jpg" alt="Azure image" style="height: 10%; width: 100%;">

        """, unsafe_allow_html=True)

    st.title('Fundamentals statistics for Data Scientist and Analyst')


    st.subheader('Random Variables')
    st.markdown('**Random variables** is a way to map the outcomes of random processes, example :')
    st.markdown('**Flipping coin** heads or tails')
    st.markdown('Statistically, this process can be defined as the following :')
    st.image('https://www.mathsisfun.com/data/images/random-variable-1.svg',use_column_width=True)
    st.markdown('In this experiment, there is 2 possible outcomes : O or 1. Each time you repeat a the random process is referred as an **event**.'
                'the chance of an event occuring is the **probability**. A probability of an event is the likelihood that a random variable takes a specific value, in'
                'the flip coin example, the likelihood of getting heads or tails is the same :')
    st.image('https://miro.medium.com/max/875/1*yKkymQ4HqNzx1WJbFM-9cg.png')

    st.subheader('Mean, Variance & Starndard Deviation')
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('First, before talking about these statistics, it is important to understand the concepts of **population** and **sample**.')
        st.markdown('What is a **population** ?')
        st.markdown('=> A population is the **set of all observation** available in your data (all individuals, objects, products etc.')
        st.markdown('What is a **sample** ?')
        st.markdown('=> A Sample is a **subset of the population**, for exemple if a company has 10.000 customers, we can create an analysis only on 1000 customers.'
                    'Generally, in a company context, we work on sample before working on the whole population because it is usefull to avoid ressources issues (exemple: we do not'
                    'have to deal directly with the **Big Data**)')
        st.image('https://www.programsbuzz.com/sites/default/files/inline-images/populationvssample-e1556351520474.png',use_column_width=True)
        st.markdown('Now you can understand that working on a sample is better because less exepensive in computation ressources.'
                    'But it is important that **the sample needs to be a true representation of the whole population**, then the sample neets to be **unbiased**.'
                    'To do that, some statisticals samplings techniques exists such as :')
        st.markdown('* **Random Sampling** : Simplify choose a random set of the population to build the sample.')
        st.markdown('* **Systematic Sampling** : It uses a patern for sample selection. We devide the **population size** by the **sample size**.')
        st.markdown('* **Stratified Sampling** : Divide the population into **subgroups**, then samples are taken from each subgroup **following a ratio**')
        st.markdown('* **Cluster Sampling** : The population is divided into **clusters** with same similarities. Then select a **random sample** from these clusters to form a sample')
        st.markdown('* **Weighted Sampling** : The sample is build **using rules directly on the data characteristics**. For example, we want to have 50% male and 50% female in our sample.')

    with col2:
        st.markdown('Now why we do need to sample the data, lets have a look at the differents trivial statistics')
        st.markdown('* **Mean** : The mean of the sample is defined as the following :')
        st.image('https://miro.medium.com/max/875/1*97xrJnzgY0nabQF1yCG-tQ.png',use_column_width=True)
        st.markdown('* **Variance** : Measure how far the data points spread out from the average value.')
        st.image("https://miro.medium.com/max/875/1*MtRN-SST_josB7RY9AqWMA.png", use_column_width=True)
        st.markdown('* **Standard Deviation** : Square root of the variance. It is generaly more usefull than the **variance**'
                    'because it follows the same unit as the datapoints.')
        st.image('https://miro.medium.com/max/875/1*m4UE4oDLL7ysLUAbfSmbag.png',use_column_width=True)
        st.markdown('* **Covariance** : Measure the variability of two randoms variables and describe. It also measure and describe the'
                    'relationship between 2 variables. The covariance can take **positive or negative values as well as 0**.'
                    '<br>'
                    'A **positive** covariance indicates that 2 variables **tend to vary in the same direction**.'
                    '<br>'
                    'A **negative covariance indicates that 2 variables **tend to vary in opposite directions**.'
                    '<br>'
                    'A **0** covariance means that **theres no relationship between the 2 variables**.')
        st.image('https://miro.medium.com/max/875/1*Jaov1ABZH4HAHE3cmz_eyQ.png', use_column_width=True)
        st.markdown('* **Correlation** : Measure both the **relationship** but also the **strength** and the **direction** of linears variables.'
                    'The **correlation range is between -1 and 1**. A correlation of 1 variable with the same variable is 1.'
                    'WARNING : This relationship shouldnt serve you to conclude that one variable causes a change in the other')
        st.image('https://miro.medium.com/max/875/1*k96hYXHRfiH7XGBWgffQjQ.png',use_column_width=True)

    st.subheader('Probabbility Distributions Functions (pdf)')
    st.markdown('What is a probability distribution function ?')
    st.markdown('=> It is a function that describes **all the possible values, the sample space and the corresponding probabilities that a random variable can take**.'
                'It is also known as **probability density**.'
                '<br>'
                'Note that every pdf needs to satisfy the following criteria :')
    st.image('https://miro.medium.com/max/1400/1*jwC75xVvcFg7iXUxfaTNFw.png', use_column_width=True)
    st.markdown('**Probability functions** are usually classified into two categories : **discrete** and **continuous** :')
    st.markdown('* **discrete** when dealing with **countable** sample space such as the coins example.')
    st.markdown('* **continuous** when dealing continuous sample space.')
    st.markdown('Many **discrete ditributions exists** such as **Bernouilli, Binomiale, Poisson, Discrete Uniform**.')
    st.markdown('Many **continuous distributions exists** such as **Normal, Coutinuous uniform and Gauchy**;')

    st.subheader('PDF - Binomial Distribution - Discrete')
    st.markdown('The binomial distribution is the discrete probability of a boolean event occurs n-times.')
    st.markdown('**sucess** = p')
    st.markdown('**Failure** = 1 - p')
    st.markdown('If a random variable X follows **binomial distribution**, then the probability of observing **K successes in **n** independant trials can be'
                'expressed as the following **density function** :')
    st.image('https://miro.medium.com/max/875/1*llaosjWmH_0huR5Z80XTSw.png',use_column_width=True)
    st.markdown('The **binomial distribution is usefull when you analyze the result of *a bollean event reppeatted n '
                'time** (The events must be independants)')
    st.markdown('<u> **Binomial distribution Mean & Variance** : </u>',unsafe_allow_html=True)
    st.image('https://miro.medium.com/max/875/1*la5m94kDTYUhEB2CExi8_w.png',use_column_width=True)
    st.markdown('<u>Example </u>: with a number of trial equal to 8 and a probability of success of each trial = 16%', unsafe_allow_html=True)
    st.image('https://miro.medium.com/max/875/1*68nMYVFT0e5VsMBf8c226g.png', use_column_width=True)

    st.subheader('PDF - Poisson Distribution - Discrete')
    st.markdown('The Poisson distribution is a **discrete** probability of events occurring in a specified time periods.'
                'It follows the following probability (with **k** events):')
    st.image('https://miro.medium.com/max/875/1*nDKMS-M07qbNPmRK6Z8OeA.png',use_column_width=True)
    st.markdown('<u> Poisson Distribution Mean & Variance </u>', unsafe_allow_html=True)
    st.image('https://miro.medium.com/max/875/1*2HtMzd1HbGzcSWXZEpU1xw.png',use_column_width=True)








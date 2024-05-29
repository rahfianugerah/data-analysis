import streamlit as st
import dataperhour
import datauser
import dataseason
import datatime

st.write(
    """
    # Bike Sharing Dashboard
    Bike Sharing Data Analysis Project
    """
)

with st.sidebar:
    st.write(
        """
            # Bike Sharing Dashboard
            Bike Sharing Data Analysis Project

            Naufal Rahfi Anugerah
        """
    )

st.write(
    """
        ### Question 1
        Which users use bicycles the most? is it casual or registered?

        From the results of the analysis below, the most users are registered users, where registered users account for more than 80% of the total, namely more than 2 million registered users for bicycle rental.
    """
)

st.plotly_chart(datauser.fig)

st.write(
    """
        ### Question 2
        At what time of day are there the most bicycle rental users and at what time of day are there the least?

        Based on the analysis and visuals below, many cyclists rent bicycles at 17:00 hours, with more than 300,000 users. On the other hand, fewer users rent bicycles at 4:00 in the morning.
    """
)
st.plotly_chart(dataperhour.fig)

st.write(
    """
        ### Question 3
        What season are there most bicycle rentals?

        The analysis shows that fall is the most desirable time for users to rent a bicycle. This could be due to the generally cooler and more comfortable weather for cycling, as well as the beautiful natural scenery during autumn with leaves changing colors. Summer ranked second, probably due to the warm weather and school vacations leading to an increase in outdoor activities. Winter and spring ranked last, perhaps due to more unpredictable weather and a lack of interest in cycling under more extreme weather conditions. As such, this information can help bike rental service providers to organize their stock and marketing strategies according to the higher demand during the fall and summer seasons.
    """
)
st.plotly_chart(dataseason.fig)

st.write(
    """
        ### Question 4
        How has the company's sales performance been in 2011 - 2012?

        It can be inferred from the visualization that the number of orders peaks in September, most likely due to seasonal factors or promotions that attract more customers. In contrast, there is a significant drop in the number of orders in November and December
    """
)
st.plotly_chart(datatime.fig)

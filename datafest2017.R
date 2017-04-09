family_comp1 <- cleanedData %>% 
  filter(srch_children_cnt == 0 & srch_adults_cnt == 2 & srch_rm_cnt == 1)

data_cleaned_couples_date <- data_cleaned_couples %>% 
   filter(is_package == 0)

cleanedData_package <- cleanedData %>% 
  filter(is_package == 0)
View(cleanedData_package)



family_comp2 <- cleanedData %>% 
  filter(srch_children_cnt == 1:3 & srch_adults_cnt == 2 & srch_rm_cnt == 1:2) %>% 
  

family_comp3 <- cleanedData %>% 
  filter(srch_children_cnt == 0 & srch_adults_cnt == 1 & srch_rm_cnt == 1)

family_comp4 <- cleanedData %>% 
  filter(srch_children_cnt == 1:3 & srch_adults_cnt == 1 & srch_rm_cnt == 1:2)

#parced by city

family_comp1_parsedcity <- cleanedData %>% 
  filter(srch_children_cnt == 0 & srch_adults_cnt == 2 & srch_rm_cnt == 1) %>% 
  filter(user_location_city == "LOS ANGELES" | 
           user_location_city == "NEW YORK" |  
           user_location_city == "HOUSTON" | 
           user_location_city == "CHICAGO" | 
           user_location_city == "CALGARY" | 
           user_location_city == "BROOKLYN" |
           user_location_city == "SAN FRANCISCO" |
           user_location_city == "SEATTLE" |
           user_location_city == "MIAMI" |
           user_location_city == "VANCOUVER" |
           user_location_city == "MONTREAL" |
           user_location_city == "SAN JOSE" |
           user_location_city == "DENVER" |
           user_location_city == "ATLANTA")

family_comp2_parsedcity <- cleanedData %>% 
  filter(srch_children_cnt == 1:3 & srch_adults_cnt == 2 & srch_rm_cnt == 1:2) %>% 
  filter(user_location_city == "LOS ANGELES" | 
           user_location_city == "NEW YORK" |  
           user_location_city == "HOUSTON" | 
           user_location_city == "CHICAGO" | 
           user_location_city == "CALGARY" | 
           user_location_city == "BROOKLYN" |
           user_location_city == "SAN FRANCISCO" |
           user_location_city == "SEATTLE" |
           user_location_city == "MIAMI" |
           user_location_city == "VANCOUVER" |
           user_location_city == "MONTREAL" |
           user_location_city == "SAN JOSE" |
           user_location_city == "DENVER" |
           user_location_city == "ATLANTA")
  
  
  family_comp3_parsedcity <- cleanedData %>% 
  filter(srch_children_cnt == 0 & srch_adults_cnt == 1 & srch_rm_cnt == 1) %>% 
  filter(user_location_city == "LOS ANGELES" | 
           user_location_city == "NEW YORK" |  
           user_location_city == "HOUSTON" | 
           user_location_city == "CHICAGO" | 
           user_location_city == "CALGARY" | 
           user_location_city == "BROOKLYN" |
           user_location_city == "SAN FRANCISCO" |
           user_location_city == "SEATTLE" |
           user_location_city == "MIAMI" |
           user_location_city == "VANCOUVER" |
           user_location_city == "MONTREAL" |
           user_location_city == "SAN JOSE" |
           user_location_city == "DENVER" |
           user_location_city == "ATLANTA")

family_comp4_parsedcity <- cleanedData %>% 
  filter(srch_children_cnt == 1:3 & srch_adults_cnt == 1 & srch_rm_cnt == 1:2) %>% 
  filter(user_location_city == "LOS ANGELES" | 
           user_location_city == "NEW YORK" |  
           user_location_city == "HOUSTON" | 
           user_location_city == "CHICAGO" | 
           user_location_city == "CALGARY" | 
           user_location_city == "BROOKLYN" |
           user_location_city == "SAN FRANCISCO" |
           user_location_city == "SEATTLE" |
           user_location_city == "MIAMI" |
           user_location_city == "VANCOUVER" |
           user_location_city == "MONTREAL" |
           user_location_city == "SAN JOSE" |
           user_location_city == "DENVER" |
           user_location_city == "ATLANTA")


#code used to separate out hot cities
filter(user_location_city == "LOS ANGELES" | 
         user_location_city == "NEW YORK" |  
         user_location_city == "HOUSTON" | 
         user_location_city == "CHICAGO" | 
         user_location_city == "CALGARY" | 
         user_location_city == "BROOKLYN" |
         user_location_city == "SAN FRANCISCO" |
         user_location_city == "SEATTLE" |
         user_location_city == "MIAMI" |
         user_location_city == "VANCOUVER" |
         user_location_city == "MONTREAL" |
         user_location_city == "SAN JOSE" |
         user_location_city == "DENVER" |
         user_location_city == "ATLANTA")



write.csv(family_comp1_parsedcity, file = "family_comp1_parsedcity.csv")


write.csv(family_comp2_parsedcity, file = "family_comp2_parsedcity.csv")


write.csv(family_comp3_parsedcity, file = "family_comp3_parsedcity.csv")

write.csv(family_comp4_parsedcity, file = "family_comp4_parsedcity.csv")

test_familycomp2_ny_bos <- filter(family_comp2, user_location_city == "NEW YORK" | user_location_city == "BOSTON") 
  

View(test_familycomp2_ny_bos_income)

test_familycomp2_ny_bos_income <- test_familycomp2_ny_bos %>% 
                                     if (user_location_city == "NEW YORK" %>% 
                                      test_familycomp2_ny_bos$newcolumn <- 60850)
                                       
#fix y-axis labels
family_comp1_parsedcity$hist_price_band <- factor(family_comp1_parsedcity$hist_price_band, levels=c("VL", "L", "M", "H", "VH"))   

                                       
                                       
family_comp2_parsedcity$hist_price_band <- factor(family_comp2_parsedcity$hist_price_band, levels=c("VL", "L", "M", "H", "VH"))  

family_comp3_parsedcity$hist_price_band <- factor(family_comp3_parsedcity$hist_price_band, levels=c("VL", "L", "M", "H", "VH"))  

family_comp4_parsedcity$hist_price_band <- factor(family_comp4_parsedcity$hist_price_band, levels=c("VL", "L", "M", "H", "VH"))   

family_comp4_parsedcity$hist_price_band <- factor(family_comp4_parsedcity$hist_price_band, levels=c("VL", "L", "M", "H", "VH"))   

family_comp1_parsedcity$hist_price_band <- factor(family_comp1_parsedcity$hist_price_band, levels=c("VL", "L", "M", "H", "VH"))   


#into plot note to self uhhh check that data frame names are consistent ya dummy (where are people staying? why are they staying there?)

ggplot(data=family_comp1_parsedcity, aes(x = user_location_city, y = hist_price_band, fill = prop_starrating)) +
  geom_tile()  + geom_raster() +
  labs(x="User City", y="Pricing by Category", title="Where are people staying and why are they staying there?") +
theme(axis.text.x = element_text(angle=65, vjust=0.6))



ggplot(data=family_comp2_parsedcity, aes(x = user_location_city, y = hist_price_band, fill = prop_starrating)) +
          geom_tile()  + geom_raster() +
  labs(x="User City", y="Pricing by Category", title="Where are people staying and why are they staying there?") +
  theme(axis.text.x = element_text(angle=65, vjust=0.6))


ggplot(data=family_comp3_parsedcity, aes(x = user_location_city, y = hist_price_band, fill = prop_starrating)) +
  geom_tile()  + geom_raster() +
  labs(x="User City", y="Pricing by Category", title="Where are people staying and why are they staying there?") +
  theme(axis.text.x = element_text(angle=65, vjust=0.6))


ggplot(data=family_comp4_parsedcity, aes(x = user_location_city, y = hist_price_band, fill = prop_starrating)) +
  geom_tile()  + geom_raster() +
  labs(x="User City", y="Pricing by Category", title="Where are people staying and why are they staying there?") +
  theme(axis.text.x = element_text(angle=65, vjust=0.6))



#fix y-axis labels

family_comp2$hist_price_band <- factor(family_comp2$hist_price_band, levels=c("VL", "L", "M", "H", "VH"))

#activity on the site (intro step) <- push the new item as quickly as possible
ggplot(data=family_comp1_final, aes(x = user_location_city, y = prop_starrating, fill = cnt)) +
  geom_tile() +
labs(x="User City", y="Star Rating", title="How Long do EXPEDIA Users Spend Searching for Hotels?: Family Coposition 1") +
  theme(axis.text.x = element_text(angle=65, vjust=0.6))


ggplot(data=family_comp2_final3, aes(x = user_location_city, y = prop_starrating, fill = cnt)) +
  geom_tile() +
  labs(x="User City", y="Star Rating", title="How Long do EXPEDIA Users Spend Searching for Hotels?: Family Compostion 2") +
  theme(axis.text.x = element_text(angle=65, vjust=0.6))


ggplot(data=family_comp3_final3, aes(x = user_location_city, y = prop_starrating, fill = cnt)) +
  geom_tile() +
  labs(x="User City", y="Star Rating", title="How Long do EXPEDIA Users Spend Searching for Hotels?: Family composition 3") +
  theme(axis.text.x = element_text(angle=65, vjust=0.6))


ggplot(data=family_comp4_final3, aes(x = user_location_city, y = prop_starrating, fill = cnt)) +
  geom_tile() +
  labs(x="User City", y="Star Rating", title="How Long do EXPEDIA Users Spend Searching for Hotels?: Family Compostheme(axis.text.x = element_text(angle=65, vjust=0.6))
ition 4?") +
  


#showing that packages are considered "value" items
# Histogram on a Categorical variable

ggplot(data=family_comp3_final3, aes(x = user_location_city, y = income, fill = is_package)) +
  geom_bar(stat = "identity") + 
  labs(title="Histogram on Categorical Variable", 
       subtitle="Across All Family Compositions")  +
  labs(x="Purchased as Package?", y="Income", title="Who is Buying Packages?") +
  theme(axis.text.x = element_text(angle=65, vjust=0.6))


#
ggplot(data=family_comp3_final3, mapping = aes(x = income, color = is_package )) +
  geom_density() + facet_wrap(~is_package)


#testing
theme_set(theme_classic())
ggplot(data=family_comp3_final3, aes(x = user_location_city, y = income)) +
  +  geom_bar(stat = "identity") 


# Histogram on a Categorical variable
ggplot(data=family_comp3_final3, aes(x = user_location_city, y = income, fill = is_package)) +
  geom_bar(stat = "identity") + 
  labs(title="Histogram on Categorical Variable", 
  subtitle="Manufacturer across Vehicle Classes") 


#fixes boolean issue and wrecks the data set
final_fix <- lapply(family_comp1_final, factor, levels = c(0, 1), labels = c("No", "Yes"))

final_final <- inner_join(family_comp1_final2, 
                          family_comp1_final, 
                          by = "income")
family_comp1_final2$income[family_comp1_final2$income %in% family_comp1_final$income] <- family_comp1_final$income

#showing that packages are considered "value" items
ggplot(data=family_comp3_final3, mapping = aes(x = is_package, y = income)) +
  geom_bar(stat = "identity") +
  labs(x="Purchased as Package?", y="Income", title="Who is Buying Packages?")











testing_frame <- cleanedData %>% 
  filter(user_location_city == "LOS ANGELES" | 
           user_location_city == "NEW YORK" |  
           user_location_city == "HOUSTON" | 
           user_location_city == "CHICAGO" | 
           user_location_city == "CALGARY" | 
           user_location_city == "BROOKLYN" |
           user_location_city == "SAN FRANCISCO" |
           user_location_city == "SEATTLE" |
           user_location_city == "MIAMI" |
           user_location_city == "VANCOUVER" |
           user_location_city == "MONTREAL" |
           user_location_city == "SAN JOSE" |
           user_location_city == "DENVER" |
           user_location_city == "ATLANTA")

ggplot(data=testing_frame, aes(x = user_location_city, y = popularity_band, fill = hist_price_band)) +
     geom_tile() +
     labs(x="User City", y="Popuarity Ranking", title="Who is Booking Across All Family Compositions?") +
  theme(axis.text.x = element_text(angle=65, vjust=0.6))


testing_frame$popularity_band <- factor(testing_frame$popularity_band, levels=c("VL", "L", "M", "H", "VH"))   

ggplot(data=family_comp1_parsedcity, aes(x = user_location_city, y = popularity_band, fill = hist_price_band)) +
  geom_tile()  + geom_raster() +
  labs(x="User City", y="Popularity of Product", title="Where are people staying and why are they staying there?") +
  theme(axis.text.x = element_text(angle=65, vjust=0.6))

ggplot(data=testing_frame, aes(x = user_location_city, y = prop_starrating, fill = cnt)) +
  geom_tile() +
  labs(x="User City", y="Star Rating", title="How Long do EXPEDIA Users Spend Searching for Hotels?: All Families") +
  theme(axis.text.x = element_text(angle=65, vjust=0.6))











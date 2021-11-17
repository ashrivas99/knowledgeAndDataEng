
queries = {
    "1": """
prefix football: <http://www.cs7is1.org/ontologies/football-ontology-3#>

select ?players_entity ?country ?country_entity ?gdpValue
where {
    ?competiton_entity football:type ?tier;
                       football:competition_id ?competition_id .
    ?club_entity football:domestic_competition_id ?competition_id;
                 football:club_id ?club_id .
    ?players_entity football:current_club_id ?club_id;
                    a football:Players;
                    football:country_of_birth ?country.
    ?country_entity football:country ?country;
                    football:gdpValue ?gdpValue
    FILTER(?tier = "first_tier" && ?gdpValue >7.33E+10) .
}
""",

    "2": """
prefix football: <http://www.cs7is1.org/ontologies/football-ontology-3#>

select (COUNT(?players_entity) as ?Count_players) ?country_entity_who ?obesity ?gdpValue

where {
    ?competiton_entity football:type ?tier;
                       football:competition_id ?competition_id .
    FILTER(?tier = "first_tier") .
    ?club_entity football:domestic_competition_id ?competition_id;
                 football:club_id ?club_id .
    ?players_entity football:current_club_id ?club_id;
                    a football:Players;
                    football:country_of_birth ?country.
    ?country_entity_gdp football:country ?country;
                        football:gdpValue ?gdpValue.
    ?country_entity_who football:who_country ?country;
                        football:Prevalence_of_obesity_among_children ?obesity.
}

GROUP BY ?country_entity_who ?obesity ?gdpValue
""",

    "3": """
prefix football: <http://www.cs7is1.org/ontologies/football-ontology-3#>

select ?countryName  (SUM(?stadSeats) AS ?totalStadiumSeats)
where {
    ?competiton_entity football:competition_id ?compID ;
                       football:country_name ?countryName.
    ?club_entity football:domestic_competition_id ?compID;
                 football:stadium_seats ?stadSeats .
} GROUP BY(?countryName) ORDER BY DESC(?totalStadiumSeats)
""",

    "4": """
prefix football: <http://www.cs7is1.org/ontologies/football-ontology-3#>

select ?club_pretty_name ?coach_name (SUM(?fee) as ?TotalFee)
where {
    ?club_entity a football:Clubs;
                 football:club_pretty_name ?club_pretty_name;
                 football:coach_name ?coach_name.

    ?transfer_entity a football:Football_Transfers;
               football:fee_cleaned ?fee;
                football:club_transferrred_to_name ?club_pretty_name.
}
GROUP BY ?coach_name ?club_pretty_name
ORDER BY DESC (?TotalFee)

""",

    "5": """
prefix football: <http://www.cs7is1.org/ontologies/football-ontology-3#>

select
?player_name (COUNT(?appearance_id) as ?Appearances) (AVG(?minutes_played) AS ?avg)
where {
    ?tf_entity a football:Football_Transfers;
               football:player_name ?player_name.

    ?players_entity a football:Players;
                    football:players_pretty_name ?player_name;
                    football:player_id ?player_id.
    ?appearance_entity a football:Appearances;
                       football:player_id ?player_id;
                       football:appearance_id ?appearance_id;
                       football:minutes_played ?minutes_played.
}
GROUP BY ?player_name
""",


    "6": """
prefix football: <http://www.cs7is1.org/ontologies/football-ontology-3#>

select
(COUNT(?appearance_id) as ?Appearances) ?country_of_birth (AVG(?minutes_played) AS ?Average_minutes_played) ?life_expectancy
where {
    ?players_entity a football:Players;
                    football:players_pretty_name ?player_name;
                    football:player_id ?player_id;
                    football:country_of_birth ?country_of_birth.

    ?appearance_entity a football:Appearances;
                       football:player_id ?player_id;
                       football:appearance_id ?appearance_id;
                       football:minutes_played ?minutes_played.

    ?who_entity a football:WHO;
                football:who_country ?country_of_birth;
                football:LifeExpectancy ?life_expectancy.
}
GROUP BY ?country_of_birth ?life_expectancy
ORDER BY DESC (?Appearances)

""",

    "7": """
prefix football: <http://www.cs7is1.org/ontologies/football-ontology-3#>

Select (Count(?win_club_id) as ?number_of_wins) ?club_name
where {
    ?competition_entity a football:Competition;
                        football:competition_name ?competition_name;
                        football:competition_id ?competition_id.
    FILTER(?competition_name= "uefa-champions-league")

    ?games_entity a football:Games;
            football:competition_code ?competition_id;
            football:game_id ?game_id;
            football:win_club_id ?win_club_id.

    ?club_entity a football:Clubs;
            football:club_id ?win_club_id;
            football:club_pretty_name ?club_name.

}
GROUP BY ?club_name
ORDER BY DESC (?number_of_wins)

""",

    "8": """
prefix football: <http://www.cs7is1.org/ontologies/football-ontology-3#>

Select ?player_pretty_name ?country_of_birth ?gdp_value_birth ?country_of_citizenship ?gdp_value_citizenship
where{
    ?player_entity a football:Players;
                   football:players_pretty_name ?player_pretty_name;
                   football:country_of_birth ?country_of_birth;
                   football:country_of_citizenship ?country_of_citizenship.

    ?gdp_entity_birth a football:GDP;
                football:country ?country_of_birth;
                football:gdpValue ?gdp_value_birth.

    ?gdp_entity_citizenship a football:GDP;
                football:country ?country_of_citizenship;
                football:gdpValue ?gdp_value_citizenship.

    FILTER (?gdp_value_birth < ?gdp_value_citizenship)
}

""",

    "9": """
prefix football: <http://www.cs7is1.org/ontologies/football-ontology-3#>

select ?country ?gdpValue ?densityDocs
where {
    ?gdp_entity football:country ?country;
                football:gdpValue ?gdpValue;
                a football:GDP.
   ?who_entity football:who_country ?country;
               football:Density_of_medical_doctors ?densityDocs;
               a football:WHO.
}
ORDER BY DESC (?densityDocs)

""",

    "10": """
prefix football: <http://www.cs7is1.org/ontologies/football-ontology-3#>

select (SUM(?fee) AS ?totalfee) ?club_name
where {
    ?tf_entitiy a football:Football_Transfers;
                football:fee_cleaned ?fee;
                football:club_transferred_from_name ?club_name.
    ?club_entity football:club_pretty_name ?club_name .
}
GROUP BY ?club_name
ORDER BY DESC (?totalfee)

"""


}

CREATE TABLE
    COMMERCIAL_DISTRICT (
        id INT AUTO_INCREMENT PRIMARY KEY,
        city VARCHAR(50) NOT NULL,
        district VARCHAR(50) NOT NULL,
        sub_district VARCHAR(50) NOT NULL,
        main_category VARCHAR(50),
        sub_category VARCHAR(50),
        detail_category VARCHAR(50),
        national_density VARCHAR(50),
        city_density VARCHAR(50),
        district_density VARCHAR(50),
        sub_district_density VARCHAR(50),
        market_size VARCHAR(50),
        average_sales VARCHAR(50),
        average_operating_cost VARCHAR(50),
        average_food VARCHAR(50),
        average_employee VARCHAR(50),
        average_rental VARCHAR(50),
        average_tax VARCHAR(50),
        average_family_employee VARCHAR(50),
        average_ceo VARCHAR(50),
        average_etc VARCHAR(50),
        average_payment_cost VARCHAR(50),
        usage_count VARCHAR(50),
        average_profit_amount VARCHAR(50),
        -- average_profit_percent VARCHAR(50),
        most_profitable_day VARCHAR(50),
        day_percent VARCHAR(50),
        sales_monday VARCHAR(50),
        sales_tuesday VARCHAR(50),
        sales_wednesday VARCHAR(50),
        sales_thursday VARCHAR(50),
        sales_friday VARCHAR(50),
        sales_saturday VARCHAR(50),
        sales_sunday VARCHAR(50),
        most_profitable_time VARCHAR(50),
        time_percent VARCHAR(50),
        sales_06_09 VARCHAR(50),
        sales_09_12 VARCHAR(50),
        sales_12_15 VARCHAR(50),
        sales_15_18 VARCHAR(50),
        sales_18_21 VARCHAR(50),
        sales_21_24 VARCHAR(50),
        sales_24_06 VARCHAR(50),
        dominant_gender VARCHAR(50),
        dominant_gender_percent FLOAT,
        dominant_age_group VARCHAR(50),
        most_visitor_age VARCHAR(50),
        male_20s FLOAT,
        male_30s FLOAT,
        male_40s FLOAT,
        male_50s FLOAT,
        male_60s FLOAT,
        female_20s FLOAT,
        female_30s FLOAT,
        female_40s FLOAT,
        female_50s FLOAT,
        female_60s FLOAT,
        total_male_percent FLOAT,
        total_female_percent FLOAT,
        top_menu_1 VARCHAR(50),
        top_menu_2 VARCHAR(50),
        top_menu_3 VARCHAR(50),
        top_menu_4 VARCHAR(50),
        top_menu_5 VARCHAR(50),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    );

drop table commercial_district;
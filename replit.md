# NBFC Analytics Dashboard

## Overview

This is a comprehensive analytics dashboard for Non-Banking Financial Companies (NBFCs) built with Python Dash. The application provides real-time insights into portfolio performance, customer segmentation, collections management, branch operations, and future projections. The dashboard features five main modules: Portfolio Overview, Customer Segmentation, Collections & Risk, Branch Performance, and Future Projections, all presented through interactive visualizations and KPI cards.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture

**Framework**: Dash with Bootstrap Components
- Multi-tab interface using `dcc.Tabs` for navigation between five analytical modules
- Responsive grid layout using `dash-bootstrap-components` with the Bootstrap theme
- Custom CSS styling for KPI cards with hover effects and consistent design system
- Dynamic content rendering based on tab selection using callback-controlled visibility

**Component Organization Pattern**:
- Separated layout definitions (`layout/` directory) from business logic (`callbacks/` directory)
- Each module (portfolio, segmentation, collections, branch, projections) has dedicated layout and callback files
- Single-page application with conditional rendering to avoid re-mounting components

**Visualization Library**: Plotly for all charts and graphs
- Line charts for trend analysis (AUM, disbursements, NPA over time)
- Bar charts for comparative analysis (branch performance, DPD buckets)
- Pie charts for distribution visualization (product mix)
- Scatter plots for forecasting and projections

### Backend Architecture

**Data Generation**: Synthetic data generator instead of database
- `generate_nbfc_data()` creates mock loan portfolio data with realistic distributions
- `generate_time_series_data()` produces monthly trend data for 36 months
- NumPy-based random generation with seeded values for reproducibility
- In-memory data processing without persistent storage

**Business Logic Layer**: Utility functions for KPI calculations
- Modular calculation functions in `utils/kpi_functions.py` (AUM, PAR, collection efficiency, NPA percentage)
- Pandas-based aggregations for branch performance and customer segmentation
- DPD (Days Past Due) bucket analysis for risk assessment

**Callback Architecture**: Event-driven updates using Dash callbacks
- Tab-based conditional rendering to optimize performance
- Multiple outputs per callback to minimize re-renders
- Input validation checks (e.g., `if tab != 'portfolio'`) to prevent unnecessary computations
- Separate callback registration per module for maintainability

**Forecasting Module**: Machine learning integration
- Linear regression models from scikit-learn for AUM, disbursement, and NPA forecasting
- Historical data split (up to October 2025) for training
- User-configurable forecast horizon (3-24 months) via slider input
- Future date generation using pandas DateOffset

### Design Patterns

**Separation of Concerns**:
- Layout files define UI structure only
- Callback files handle data processing and interactivity
- Utility modules contain reusable business logic
- No data manipulation in layout definitions

**Module Pattern**:
- Each analytical module is self-contained with its own layout and callbacks
- `register_callbacks()` pattern allows clean callback registration in main app
- Prevents callback ID conflicts across modules

**Performance Optimization**:
- Lazy rendering using display:none instead of destroying components
- Data generation only when tab is active (tab value checks in callbacks)
- Memoization opportunity exists for expensive calculations (not currently implemented)

## External Dependencies

### Core Framework
- **Dash** (>=2.14.0): Web application framework for building analytical dashboards
- **dash-bootstrap-components** (>=1.5.0): Bootstrap-based UI components for Dash

### Data Processing & Analysis
- **pandas** (>=2.1.0): DataFrame operations, aggregations, and time series handling
- **numpy** (>=1.24.0): Numerical computations and random data generation
- **scikit-learn** (>=1.3.0): Linear regression models for forecasting module

### Visualization
- **plotly** (>=5.18.0): Interactive charting library for all visualizations

### Infrastructure
- Standard Python web server (built into Dash)
- No database system (uses in-memory synthetic data)
- No external API integrations
- No authentication/authorization system implemented

### Future Integration Points
The architecture supports adding:
- Database integration (PostgreSQL/MySQL) by replacing data_loader functions
- API endpoints for real-time data feeds
- Export functionality for reports (PDF/Excel)
- User authentication layer (Flask-Login compatible)
- Caching layer (Redis) for performance optimization
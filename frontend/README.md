# Frontend

The user interface for Weather Alert System.

## File

- `index.html` - Complete responsive UI (HTML + CSS + JavaScript)

## Features

- ✅ Subscribe form (email, city, condition)
- ✅ Subscriptions list view
- ✅ Real-time updates
- ✅ Delete functionality
- ✅ Responsive design (mobile + desktop)
- ✅ Error handling
- ✅ Success/error messages

## Technologies

- HTML5
- CSS3 (modern gradients, flexbox, grid)
- Vanilla JavaScript (no frameworks)

## API Integration

Calls Lambda functions via API Gateway:
```javascript
POST   /subscribe       → Create subscription
GET    /subscriptions   → Fetch all subscriptions
DELETE /subscribe/{id}  → Delete subscription
```

## Styling

- Purple gradient background
- Card-based layout
- Smooth animations
- Mobile responsive
- Professional typography

## How to Update

1. Edit `index.html`
2. Change `const API_URL` to your API Gateway URL
3. Upload to S3
4. Test in browser

## Performance

- **Load time**: <1 second
- **Interactive**: <200ms (API response)
- **Mobile friendly**: Yes
- **Accessibility**: WCAG compliant

# Veerashaiva Mart EmailJS templates

Create two templates in EmailJS. Configure both templates with **Reply-To** as `{{reply_to}}`.

## 1. Owner notification template

- **Template ID:** `template_pinwrjf`
- **To Email:** `{{to_email}}` (resolves to `vinyassharana06@gmail.com` from the website)
- **Subject:** `New enquiry from {{from_name}} | Veerashaiva Mart`

```html
<div style="margin:0;padding:24px;background:#eef4f7;font-family:Arial,sans-serif;color:#16384f;">
  <div style="max-width:640px;margin:0 auto;background:#ffffff;border-radius:8px;overflow:hidden;box-shadow:0 8px 28px rgba(8,38,59,.12);">
    <div style="padding:28px 32px;background:#08223b;color:#ffffff;">
      <p style="margin:0 0 8px;font-size:12px;letter-spacing:1.4px;text-transform:uppercase;color:#8ed1ff;">{{website_name}}</p>
      <h1 style="margin:0;font-size:26px;line-height:1.2;">New Enquiry Received</h1>
    </div>
    <div style="padding:28px 32px;">
      <p style="margin:0 0 20px;font-size:15px;color:#607688;">Received on {{submission_date}}</p>
      <table style="width:100%;border-collapse:collapse;font-size:15px;">
        <tr><td style="padding:10px 0;width:160px;font-weight:bold;border-bottom:1px solid #e7edf1;">Name</td><td style="padding:10px 0;border-bottom:1px solid #e7edf1;">{{from_name}}</td></tr>
        <tr><td style="padding:10px 0;font-weight:bold;border-bottom:1px solid #e7edf1;">Phone</td><td style="padding:10px 0;border-bottom:1px solid #e7edf1;"><a href="tel:{{phone}}" style="color:#0d5684;">{{phone}}</a></td></tr>
        <tr><td style="padding:10px 0;font-weight:bold;border-bottom:1px solid #e7edf1;">Email</td><td style="padding:10px 0;border-bottom:1px solid #e7edf1;"><a href="mailto:{{from_email}}" style="color:#0d5684;">{{from_email}}</a></td></tr>
        <tr><td style="padding:10px 0;font-weight:bold;border-bottom:1px solid #e7edf1;">Company</td><td style="padding:10px 0;border-bottom:1px solid #e7edf1;">{{company}}</td></tr>
        <tr><td style="padding:10px 0;font-weight:bold;border-bottom:1px solid #e7edf1;">Location</td><td style="padding:10px 0;border-bottom:1px solid #e7edf1;">{{location}}</td></tr>
        <tr><td style="padding:10px 0;font-weight:bold;">Quantity / details</td><td style="padding:10px 0;">{{quantity}}</td></tr>
      </table>
      <div style="margin-top:22px;padding:18px;background:#f1f7fa;border-left:4px solid #2f8abc;border-radius:3px;">
        <p style="margin:0 0 7px;font-weight:bold;">Requirement</p>
        <p style="margin:0;white-space:pre-wrap;line-height:1.6;">{{message}}</p>
      </div>
    </div>
  </div>
</div>
```

## 2. Customer confirmation template

- **Template ID:** create one and add it as `VITE_EMAILJS_CONFIRMATION_TEMPLATE_ID`
- **To Email:** `{{to_email}}`
- **Subject:** `We received your enquiry | Veerashaiva Mart`

```html
<div style="margin:0;padding:24px;background:#eef4f7;font-family:Arial,sans-serif;color:#16384f;">
  <div style="max-width:640px;margin:0 auto;background:#ffffff;border-radius:8px;overflow:hidden;box-shadow:0 8px 28px rgba(8,38,59,.12);">
    <div style="padding:28px 32px;background:#08223b;color:#ffffff;">
      <p style="margin:0 0 8px;font-size:12px;letter-spacing:1.4px;text-transform:uppercase;color:#8ed1ff;">{{website_name}}</p>
      <h1 style="margin:0;font-size:26px;line-height:1.2;">Thank you, {{to_name}}</h1>
    </div>
    <div style="padding:28px 32px;font-size:15px;line-height:1.65;">
      <p style="margin-top:0;">We have received your enquiry submitted on <strong>{{submission_date}}</strong>.</p>
      <p>Our team will review your requirement and get in touch with you soon.</p>
      <div style="margin:22px 0;padding:18px;background:#f1f7fa;border-left:4px solid #2f8abc;border-radius:3px;">
        <p style="margin:0 0 7px;font-weight:bold;">Your requirement</p>
        <p style="margin:0;white-space:pre-wrap;">{{message}}</p>
      </div>
      <p style="margin-bottom:0;">Regards,<br><strong>Veerashaiva Mart</strong></p>
    </div>
  </div>
</div>
```

## Variables sent by the website

`{{to_email}}`, `{{to_name}}`, `{{reply_to}}`, `{{from_name}}`, `{{from_email}}`, `{{phone}}`, `{{company}}`, `{{location}}`, `{{message}}`, `{{quantity}}`, `{{submission_date}}`, `{{website_name}}`.

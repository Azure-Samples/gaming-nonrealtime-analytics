---
topic: sample
languages:
  - csharp
products:
  - azure
  - azure-event-hubs
  - azure-databricks
  - azure-storage
azureDeploy: https://raw.githubusercontent.com/Azure-Samples/gaming-nonrealtime-analytics/master/azuredeploy.json
---

# Non-Realtime Analytics for Gaming - Reference Architecture

This reference architecture represents a simple analytics pipeline that you can build on Azure. It can be leveraged when you won't be tracking data that requires real-time analysis and instead you just plan to do review sessions of the data every now and then (daily, weekly, bi-weekly, monthly). The presentation layer is a dashboard that you will be able to customize at will. You could use this while you are developing your game and in production.

## Deploy

To deploy the reference architecture to your own account, use the button below.

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure-Samples%2Fgaming-nonrealtime-analytics%2Fmaster%2Fazuredeploy.json" target="_blank"><img src="https://azuredeploy.net/deploybutton.png"/></a>

Then, please see the full documentation on the [Non-real Time Dashboard Reference Architectures](https://docs.microsoft.com/gaming/azure/reference-architectures/analytics-non-real-time-dashboard) to learn how it all works.

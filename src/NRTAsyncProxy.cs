using System;
using System.IO;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Azure.WebJobs;
using Microsoft.Azure.WebJobs.Extensions.Http;
using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.Logging;
using Newtonsoft.Json;

namespace NRTAnalytics
{
    public static class NRTAsyncProxy
    {
        [FunctionName("NRTAPI")]
        [return: EventHub("ehnrtanalytics-output", Connection = "EVENTHUB_CONNECTION_STRING")]
        public static async Task<string> Run(
            [HttpTrigger(AuthorizationLevel.Function, "get", "post", Route = null)] HttpRequest req,
            ILogger log)
        {
            string version = req.Query["version"];

            string requestBody = await new StreamReader(req.Body).ReadToEndAsync();
            dynamic data = JsonConvert.DeserializeObject(requestBody);
            version = version ?? data?.version;

            // Checks that the event contains at least a "version" value
            if (version != null)
            {
                log.LogInformation($"C# HTTP trigger function processed a request. {requestBody}");
                return requestBody;
            }
            return null;
        }
    }
}

namespace DCSWorldUniversalTandem.SerialDeserial
{
    using System;
    using System.Collections.Generic;

    using System.Globalization;
    using Newtonsoft.Json;
    using Newtonsoft.Json.Converters;

    public partial class Switch
    {
        [JsonProperty("name")]
        public string Name { get; set; }

        [JsonProperty("interFaceId")]
        [JsonConverter(typeof(ParseStringConverter))]
        public long InterFaceId { get; set; }

        [JsonProperty("type")]
        public string Type { get; set; }

        [JsonProperty("states", NullValueHandling = NullValueHandling.Ignore)]
        public List<string> States { get; set; }

        [JsonProperty("currentState")]
        public string CurrentState { get; set; }
    }
}
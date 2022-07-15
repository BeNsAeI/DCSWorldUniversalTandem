namespace DCSWorldUniversalTandem.SerialDeserial
{
    using System;
    using System.Collections.Generic;

    using System.Globalization;
    using Newtonsoft.Json;
    using Newtonsoft.Json.Converters;

    public partial class ActionBuffer
    {
        [JsonProperty("role")]
        public string Role { get; set; }

        [JsonProperty("type")]
        public string Type { get; set; }

        [JsonProperty("interFaceId")]
        [JsonConverter(typeof(ParseStringConverter))]
        public long InterFaceId { get; set; }

        [JsonProperty("fromState")]
        public string FromState { get; set; }

        [JsonProperty("toState")]
        public string ToState { get; set; }

        [JsonProperty("status")]
        public string Status { get; set; }
    }
}